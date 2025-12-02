
import pretty_midi

# Create a MIDI file with the given tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define note values for the time signature (4/4, 160 BPM)
# Each beat is 0.375 seconds, bar is 1.5 seconds
beat = 0.375
bar = 1.5
note_duration = beat / 2  # 16th note

# Drums: kick (36), snare (38), hihat (42)
# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (0.0, 36, 100),     # Kick on 1
    (0.375, 42, 100),   # Hihat on 2
    (0.75, 38, 100),    # Snare on 3
    (1.125, 42, 100),   # Hihat on 4
    (1.5, 36, 100),     # Kick on 1 (next bar, but this is just the end of bar 1)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + note_duration))

# Bar 2: Full quartet starts
# Bass: Walking line in D minor, chromatic approaches
# Dm7 = D F A C
# Chromatic approach to each chord tone

bass_notes = [
    (1.5, 62, 100),   # D (Bass) - 1
    (1.875, 60, 100), # C# (approach to D) - 2
    (2.25, 62, 100),  # D (Bass) - 3
    (2.625, 64, 100), # E (approach to F) - 4
    (3.0, 65, 100),   # F (Bass) - 1
    (3.375, 63, 100), # E# (approach to F) - 2
    (3.75, 65, 100),  # F (Bass) - 3
    (4.125, 67, 100), # G (approach to A) - 4
    (4.5, 69, 100),   # A (Bass) - 1
    (4.875, 67, 100), # G# (approach to A) - 2
    (5.25, 69, 100),  # A (Bass) - 3
    (5.625, 71, 100), # B (approach to C) - 4
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + note_duration))

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Chords in D minor: Dm7, G7, Cm7, F7

piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62, 100),   # D
    (1.5, 65, 100),   # F
    (1.5, 69, 100),   # A
    (1.5, 72, 100),   # C
    (2.25, 62, 100),  # D (comp on 2)
    (2.25, 65, 100),  # F
    (2.25, 69, 100),  # A
    (2.25, 72, 100),  # C
    
    # Bar 3 (3.0 - 4.5s)
    (3.0, 71, 100),   # G
    (3.0, 74, 100),   # B
    (3.0, 77, 100),   # D
    (3.0, 81, 100),   # F
    (3.75, 71, 100),  # G (comp on 2)
    (3.75, 74, 100),  # B
    (3.75, 77, 100),  # D
    (3.75, 81, 100),  # F
    
    # Bar 4 (4.5 - 6.0s)
    (4.5, 60, 100),   # C
    (4.5, 64, 100),   # E
    (4.5, 67, 100),   # G
    (4.5, 71, 100),   # B
    (5.25, 60, 100),  # C (comp on 2)
    (5.25, 64, 100),  # E
    (5.25, 67, 100),  # G
    (5.25, 71, 100),  # B
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + note_duration))

# Sax: Motif
# The motif is a short phrase that starts and ends the intro.
# It’s a 4-note phrase that leaves something hanging.

sax_notes = [
    (1.5, 72, 100),   # C (start of the motif)
    (1.875, 76, 100), # E (up a major third)
    (2.25, 74, 100),  # D (chromatic down)
    (2.625, 72, 100), # C (resolve)
    (3.5, 72, 100),   # C (reprise the motif)
    (3.875, 76, 100), # E
    (4.25, 74, 100),  # D
    (4.625, 72, 100), # C
    (5.5, 72, 100),   # C (end on a whisper)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + note_duration))

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file to disk
midi.write("dante_intro.mid")
