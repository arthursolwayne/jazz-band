
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set key signature (F minor)
# F minor: F, Gb, Ab, Bb, C, Db, Eb
# We’ll use the key signature with 2 flats and one sharp
pm.key_signature_changes = [pretty_midi.KeySignature(key_number=22, time=0)]  # F minor

# Instrument tracks
track_drum = pretty_midi.Instrument(program=10)  # Drums
track_bass = pretty_midi.Instrument(program=33)  # Electric Bass
track_piano = pretty_midi.Instrument(program=0)  # Acoustic Piano
track_sax = pretty_midi.Instrument(program=67)   # Tenor Sax

pm.instruments = [track_drum, track_bass, track_piano, track_sax]

# Time per beat = 60 / 160 = 0.375 seconds
# Bar length = 4 beats = 1.5 seconds
# 6 seconds total

# Helper function: convert beats to seconds
def beat_to_time(beats):
    return beats * 0.375

# Bar 1: Drums only (tense intro)
# Kick on 1 and 3, snare on 2 and 4, hihats on every eighth
for i in range(8):
    time = beat_to_time(i)
    # Hihat on every eighth
    track_drum.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.375))
    # Snare on 2 and 4
    if i % 2 == 1:
        track_drum.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375))
    # Kick on 1 and 3
    if i % 4 in [0, 2]:
        track_drum.notes.append(pretty_midi.Note(velocity=110, pitch=36, start=time, end=time + 0.375))

# Bar 2-4: Full band enters
# Time starts at beat 8 (2nd bar), bar 3 and 4 continue from there

# Bass line: Walking line in F minor, chromatic
# Fm: F, Gb, Ab, Bb, C, Db, Eb
# Walking line: F - Gb - Ab - Bb - C - Db - Eb - F (repeating)
bass_notes = [71, 69, 67, 65, 62, 60, 59, 71]  # MIDI pitches of F, Gb, Ab, Bb, C, Db, Eb, F
bass_durations = [0.375] * 8
for i in range(8):
    time = beat_to_time(i + 8)
    track_bass.notes.append(pretty_midi.Note(velocity=100, pitch=bass_notes[i], start=time, end=time + bass_durations[i]))

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, C
# Dm7 = D, F, Ab, Bb (tension)
# Gm7 = G, Bb, Db, Eb (chromatic tension)
# Bbm7 = Bb, Db, Eb, F (tension)
# Comp on 2 and 4 of bars 2, 3, 4
piano_notes = [
    # Bar 2 (beats 1-4)
    [71, 67, 65, 62],  # Fm7
    [69, 71, 67, 65],  # Dm7 (2)
    [67, 65, 62, 60],  # Gm7 (3)
    [65, 60, 59, 71],  # Bbm7 (4)
    
    # Bar 3 (beats 5-8)
    [71, 67, 65, 62],  # Fm7
    [69, 71, 67, 65],  # Dm7 (2)
    [67, 65, 62, 60],  # Gm7 (3)
    [65, 60, 59, 71],  # Bbm7 (4)
    
    # Bar 4 (beats 9-12)
    [71, 67, 65, 62],  # Fm7
    [69, 71, 67, 65],  # Dm7 (2)
    [67, 65, 62, 60],  # Gm7 (3)
    [65, 60, 59, 71],  # Bbm7 (4)
]

for i, chord in enumerate(piano_notes):
    time = beat_to_time(i + 8)
    # Play all notes in the chord together
    for note in chord:
        track_piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Tenor Sax: Motif — F, Ab, Bb, C — then space, then return
# F (71), Ab (67), Bb (65), C (62) — then silence for 1 beat, then repeat

sax_notes = [
    # Bar 2 (beat 1)
    [71],
    # Bar 2 (beat 2)
    [67],
    # Bar 2 (beat 3)
    [65],
    # Bar 2 (beat 4)
    [62],
    
    # Bar 3 (beat 1) — silence
    [],
    # Bar 3 (beat 2)
    [71],
    # Bar 3 (beat 3)
    [67],
    # Bar 3 (beat 4)
    [65],
    
    # Bar 4 (beat 1)
    [62],
    # Bar 4 (beat 2)
    [71],
    # Bar 4 (beat 3)
    [67],
    # Bar 4 (beat 4)
    [65],
]

for i, note in enumerate(sax_notes):
    if note:
        time = beat_to_time(i + 8)
        track_sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=time, end=time + 0.375))

# Save the MIDI file
pm.write('Fm_intro_wayne.mid')
