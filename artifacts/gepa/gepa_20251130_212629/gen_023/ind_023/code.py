
import pretty_midi

# Create a PrettyMIDI object with a tempo of 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Create instruments for each player
# 1. Drums (Little Ray)
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Using piano for MIDI drums
drum_instrument = pretty_midi.Instrument(program=drum_program, is_drum=True)
pm.instruments.append(drum_instrument)

# 2. Bass (Marcus)
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
bass_instrument = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

# 3. Piano (Diane)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_instrument = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

# 4. Tenor Sax (Dante)
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax_instrument = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# Time in seconds per beat (60 / 160 = 0.375)
beat = 0.375
bar = beat * 4  # 1.5 seconds per bar

# Define the key: D major (D, E, F#, G, A, B, C#)
# We'll use D as the tonic, mostly diatonic with a few chromatic approaches

# *** Bar 1: Little Ray on Drums (60 seconds = 1.5 seconds) ***
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):  # 4 beats per bar
    time = i * beat
    if i % 2 == 0:  # Kick on 1 and 3
        drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
    if i % 2 == 1:  # Snare on 2 and 4
        drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1))
    # Hihat on every eighth
    drum_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05))

# *** Bar 2: Bass, Piano, and Tenor Sax join in ***
# Bass: Walking line, chromatic approach, no repeated notes
# D F# G A D (chromatic approach to D)
bass_notes = [50, 53, 55, 57, 50]  # D (50), F# (53), G (55), A (57), D (50)
for i, note in enumerate(bass_notes):
    time = beat * (i + 1)
    bass_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + beat))

# Piano: 7th chords, comp on 2 and 4
# D7 (D, F#, A, C#)
# Chord on beat 2 and 4
piano_notes = [
    [50, 53, 57, 61],  # D7 on beat 2
    [50, 53, 57, 61],  # D7 on beat 4
]
for i, chord in enumerate(piano_notes):
    time = beat * (i + 2)
    for note in chord:
        piano_instrument.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + beat/2))

# Tenor Sax: Your motif — short, memorable, space between notes
# D, F#, A, D (chromatic approach to D)
# Start it, leave it hanging, come back and finish it
sax_notes = [
    (50, 0.1),  # D
    (53, 0.1),  # F#
    (57, 0.1),  # A
    (50, 0.1),  # D
    (50, 0.1),  # D (reprise)
    (53, 0.1),  # F#
    (57, 0.1),  # A
    (50, 0.1),  # D
]

# Start time for the sax motif: beat 1 (time = 0)
start_time = 0
for note, duration in sax_notes:
    sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + duration))
    start_time += duration

# Write the MIDI file
pm.write("jazz_intro.mid")
print("MIDI file saved as 'jazz_intro.mid'")
