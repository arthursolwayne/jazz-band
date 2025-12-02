
import pretty_midi

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments for each player
drums = pretty_midi.Instrument(program=10, is_drum=True)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

# Add instruments to the MIDI file
pm.instruments = [drums, bass, piano, sax]

# Define the tempo (160 BPM) and time per beat (seconds)
tempo = 160  # beats per minute
beat_time = 60.0 / tempo  # seconds per beat
bar_time = beat_time * 4  # seconds per bar (4/4)

# Utility function to convert time to seconds
def time_to_seconds(t):
    return t * beat_time

# ---- DRUMS: Little Ray ----
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(4):
    for beat in range(4):
        time = time_to_seconds(bar * 4 + beat)
        if beat == 0 or beat == 2:
            # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            # Snare on 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hihat on every eighth note
        for eighth in range(2):
            note_time = time + (eighth * 0.5)
            note = pretty_midi.Note(velocity=60, pitch=42, start=note_time, end=note_time + 0.05)
            drums.notes.append(note)

# ---- BASS: Marcus ----
# Walking line in Fm (F, G, Ab, Bb), starting on F (MIDI 53)
bass_notes = [
    # Bar 1: F (53), G (55), Ab (56), Bb (57)
    (53, time_to_seconds(0), time_to_seconds(0) + 0.5),
    (55, time_to_seconds(0) + 0.5, time_to_seconds(0) + 1.0),
    (56, time_to_seconds(0) + 1.0, time_to_seconds(0) + 1.5),
    (57, time_to_seconds(0) + 1.5, time_to_seconds(0) + 2.0),
    
    # Bar 2: Bb (57), C (58), Db (59), Eb (60)
    (57, time_to_seconds(2.0), time_to_seconds(2.0) + 0.5),
    (58, time_to_seconds(2.0) + 0.5, time_to_seconds(2.0) + 1.0),
    (59, time_to_seconds(2.0) + 1.0, time_to_seconds(2.0) + 1.5),
    (60, time_to_seconds(2.0) + 1.5, time_to_seconds(2.0) + 2.0),
    
    # Bar 3: Eb (60), F (53), G (55), Ab (56)
    (60, time_to_seconds(4.0), time_to_seconds(4.0) + 0.5),
    (53, time_to_seconds(4.0) + 0.5, time_to_seconds(4.0) + 1.0),
    (55, time_to_seconds(4.0) + 1.0, time_to_seconds(4.0) + 1.5),
    (56, time_to_seconds(4.0) + 1.5, time_to_seconds(4.0) + 2.0),
    
    # Bar 4: Ab (56), Bb (57), C (58), Db (59)
    (56, time_to_seconds(6.0), time_to_seconds(6.0) + 0.5),
    (57, time_to_seconds(6.0) + 0.5, time_to_seconds(6.0) + 1.0),
    (58, time_to_seconds(6.0) + 1.0, time_to_seconds(6.0) + 1.5),
    (59, time_to_seconds(6.0) + 1.5, time_to_seconds(6.0) + 2.0),
]

for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# ---- PIANO: Diane ----
# Open voicings, different chord each bar, resolving on the last
def chord_notes(root, quality):
    if quality == 'm':  # minor chord
        return [root, root + 3, root + 7]
    elif quality == '7':  # dominant 7
        return [root, root + 3, root + 7, root + 10]
    elif quality == 'm7':  # minor 7
        return [root, root + 3, root + 7, root + 10]
    elif quality == 'M7':  # major 7
        return [root, root + 4, root + 7, root + 11]
    return []

# Bar 1: Fm7 -> F (MIDI 53), Ab (MIDI 56), C (MIDI 60), Eb (MIDI 63)
chord = chord_notes(53, 'm7')
for pitch in chord:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=0, end=2.0)
    piano.notes.append(note)

# Bar 2: G7 -> G (MIDI 55), B (MIDI 59), D (MIDI 62), F (MIDI 53)
chord = chord_notes(55, '7')
for pitch in chord:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=2.0, end=4.0)
    piano.notes.append(note)

# Bar 3: Abm7 -> Ab (MIDI 56), C (MIDI 60), Eb (MIDI 63), G (MIDI 67)
chord = chord_notes(56, 'm7')
for pitch in chord:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=4.0, end=6.0)
    piano.notes.append(note)

# Bar 4: Bbm7 -> Bb (MIDI 57), Db (MIDI 60), F (MIDI 53), Ab (MIDI 56)
chord = chord_notes(57, 'm7')
for pitch in chord:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=6.0, end=8.0)
    piano.notes.append(note)

# ---- SAX: Dante ----
# One short motif, haunting, with rests and space
# Motif: F (53), Bb (57), Eb (60), rest
# Bar 1: 1st beat (F), 3rd beat (Bb), 4th beat (Eb), rest on 2nd beat
note = pretty_midi.Note(velocity=110, pitch=53, start=0, end=0.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=57, start=1.5, end=2.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=60, start=2.5, end=3.0)
sax.notes.append(note)

# Bar 2: Repeat motif (shifted by 2 bars)
note = pretty_midi.Note(velocity=110, pitch=53, start=2.0, end=2.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=57, start=3.5, end=4.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=5.0)
sax.notes.append(note)

# Bar 3: Repeat motif again
note = pretty_midi.Note(velocity=110, pitch=53, start=4.0, end=4.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=57, start=5.5, end=6.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=60, start=6.5, end=7.0)
sax.notes.append(note)

# Bar 4: End with a whisper
note = pretty_midi.Note(velocity=90, pitch=53, start=6.0, end=6.5)
sax.notes.append(note)

# Save the MIDI file
pm.write("dante_russo_intro.mid")
