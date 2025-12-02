
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set key to D (no modulation)
pm.key_signature = pretty_midi.KeySignature(key_number=2)  # D major

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Time settings
# 4 bars at 160 BPM, 4/4 time
# 1 bar = 1.5 seconds (60 / 160 * 4 = 1.5)
# 1 beat = 0.375 seconds
# 16th note = 0.09375 seconds
beat_length = 0.375
bar_length = 1.5
note_duration = 0.09375  # 16th note
rest = 0.1  # 100ms of silence to create tension

# --- DRUMS: Bar 1 only (kick on 1 and 3, snare on 2 and 4, hihat on every 8th) ---
# 4/4 bar, 8 eighth notes
# Kick on 1 and 3 (beats 0 and 2)
drum_notes = [pretty_midi.note_number_to_name(36), pretty_midi.note_number_to_name(38)]  # Kick and Snare
for i in range(0, 4):
    time = i * beat_length
    if i % 2 == 0:
        # Kick on 1 and 3
        drum = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.05)
        drums.notes.append(drum)
    else:
        # Snare on 2 and 4
        drum = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.05)
        drums.notes.append(drum)

# Hi-hats on every 8th note
for i in range(0, 8):
    time = i * (beat_length / 2)
    hi_hat = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.03)
    drums.notes.append(hi_hat)

# --- BASS: Bar 1 - Chromatic walking line, no repeated notes ---
# Walking line starting on D (note 62)
bass_notes = [62, 63, 64, 65, 63, 62, 60, 59, 60, 62, 63, 64, 63, 62, 60, 59]

# Add to bass instrument
for i, pitch in enumerate(bass_notes):
    start = i * note_duration
    end = start + note_duration
    bass_note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(bass_note)

# --- PIANO: Bars 2-4, comp on 2 and 4 with 7th chords (stay out of sax's way) ---
# 7th chords on 2 and 4 of bars 2-4
# Time starts at bar 1 (1.5s) + bar 2 (1.5s) = 3.0s
# Bar 2: start at 1.5s, bar 3: 3.0s, bar 4: 4.5s

# D7: D, F#, A, C
# Gm7: G, Bb, D, F
# C7: C, E, G, Bb
# E7: E, G#, B, D
# A7: A, C#, E, G
# D7 again

chords = [
    # Bar 2, beat 2: D7
    [62, 67, 69, 60],
    # Bar 2, beat 4: Gm7
    [67, 71, 69, 65],
    # Bar 3, beat 2: C7
    [60, 64, 67, 71],
    # Bar 3, beat 4: E7
    [64, 69, 71, 62],
    # Bar 4, beat 2: A7
    [65, 69, 72, 67],
    # Bar 4, beat 4: D7
    [62, 67, 69, 60]
]

for chord in chords:
    time = (bar_length * 2) + (chord.index % 2) * beat_length  # on 2 and 4 of bars 2-4
    for pitch in chord:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + note_duration)
        piano.notes.append(note)

# --- SAX: Bars 2-4, short motif with space, leaving a question ---
# Motif: D (62) - E (64) - F# (67) - rest
# D - E - F# - (rest)
# Then return to D on beat 4 of bar 4

sax_notes = [
    # Bar 2, beat 1: D
    [62, 0.375],
    # Bar 2, beat 2: E
    [64, 0.375],
    # Bar 2, beat 3: F#
    [67, 0.375],
    # Bar 2, beat 4: rest
    [None, 0.375],
    # Bar 3: rest
    [None, 1.5],
    # Bar 4, beat 1: D
    [62, 0.375],
    # Bar 4, beat 2: E
    [64, 0.375],
    # Bar 4, beat 3: F#
    [67, 0.375],
    # Bar 4, beat 4: rest
    [None, 0.375]
]

time_start = bar_length  # start on bar 2
for pitch, duration in sax_notes:
    if pitch is not None:
        sax_note = pretty_midi.Note(velocity=100, pitch=pitch, start=time_start, end=time_start + duration)
        sax.notes.append(sax_note)
    else:
        # Add a rest by not adding a note
        pass
    time_start += duration

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file 'dante_intro.mid' has been created.")
