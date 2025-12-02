
import pretty_midi

# Initialize MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
kick = 36
snare = 38
hihat = 42

# Time in seconds
bar_length = 1.5  # 160 BPM, 4/4 time

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_pattern = [
    (kick, 0.0),  # Kick on beat 1
    (snare, 0.75),  # Snare on beat 2
    (kick, 1.5),  # Kick on beat 3
    (snare, 2.25),  # Snare on beat 4
    (hihat, 0.0),  # Hihat on 1
    (hihat, 0.375),  # Hihat on 1 &
    (hihat, 0.75),  # Hihat on 2
    (hihat, 1.125),  # Hihat on 2 &
    (hihat, 1.5),  # Hihat on 3
    (hihat, 1.875),  # Hihat on 3 &
    (hihat, 2.25),  # Hihat on 4
    (hihat, 2.625)  # Hihat on 4 &
]

for note, time in drum_pattern:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full ensemble (1.5 - 3.0s)

# Piano: 7th chords on 2 and 4. D7 on beat 2, G7 on beat 4
piano_notes = [
    (67, 1.5),  # D (root)
    (72, 1.5),  # G
    (74, 1.5),  # B
    (76, 1.5),  # D (7th)
    (72, 2.25),  # G (G7)
    (77, 2.25),  # B
    (79, 2.25),  # D
    (81, 2.25),  # F#
]

for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    (67, 1.5),   # D
    (68, 1.625), # Eb
    (70, 1.75),  # F
    (72, 1.875), # G
    (74, 2.0),   # A
    (76, 2.125), # B
    (77, 2.25),  # B
    (79, 2.375), # D
    (77, 2.5),   # B
    (76, 2.625), # B
    (74, 2.75),  # A
    (72, 2.875)  # G
]

for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Sax: Melody - your moment. One short motif, make it sing.
# Start on D (67), then G (72), then B (74), leave it hanging on G (72)
# Then come back and finish with D (67)
sax_notes = [
    (67, 1.5),   # D
    (72, 1.875), # G
    (74, 2.25),  # B
    (72, 2.625), # G (hang)
    (67, 2.875)  # D (resolve)
]

for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
