
import pretty_midi

# Create the MIDI file with tempo set to 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes mapped to MIDI note numbers
kick = 36
snare = 38
hihat = 42

# Bar 1: Drums only - 0.0 - 1.5s
# Create a sense of tension and anticipation
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (kick, 0.0, 0.5),  # Kick on 1
    (hihat, 0.0, 0.25),  # Hihat on 1
    (hihat, 0.25, 0.25),  # Hihat on 2
    (snare, 0.5, 0.5),  # Snare on 2
    (hihat, 0.5, 0.25),  # Hihat on 2
    (hihat, 0.75, 0.25),  # Hihat on 3
    (kick, 1.0, 0.5),  # Kick on 3
    (hihat, 1.0, 0.25),  # Hihat on 3
    (hihat, 1.25, 0.25),  # Hihat on 4
    (snare, 1.5, 0.5),  # Snare on 4
    (hihat, 1.5, 0.25),  # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Time signatures: 4/4, 160 BPM = 0.375 seconds per beat

# Bass line: Walking line with chromatic approaches
# Key of D: D, E, F#, G, A, B, C#, D
# Chromatic approach to each chord
bass_notes = [
    (62, 1.5, 0.375),  # D - Root
    (63, 1.875, 0.375),  # E - Chromatic approach to G
    (64, 2.25, 0.375),  # F#
    (65, 2.625, 0.375),  # G - Root
    (67, 2.875, 0.375),  # A - Chromatic approach to B
    (68, 3.25, 0.375),  # B
    (69, 3.625, 0.375),  # C# - Chromatic approach to D
    (62, 4.0, 0.375),  # D
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comping
# Key of D: D7 (D, F#, A, C#)
# Comp on 2 and 4 with some chromatic passing
piano_notes = [
    (62, 2.0, 0.375),  # D
    (67, 2.0, 0.375),  # A
    (64, 2.0, 0.375),  # F#
    (69, 2.0, 0.375),  # C#
    (62, 3.0, 0.375),  # D
    (67, 3.0, 0.375),  # A
    (64, 3.0, 0.375),  # F#
    (69, 3.0, 0.375),  # C#
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone: The melody - a short motif that starts, lingers, and resolves
# D - F# - G - (rest) - B - D - (rest) - F# - G
# Phrasing: Incomplete at first, then resolves
sax_notes = [
    (62, 1.5, 0.375),  # D
    (67, 1.875, 0.375),  # F#
    (69, 2.25, 0.375),  # G
    (62, 2.625, 0.375),  # D
    (67, 3.0, 0.375),  # F#
    (69, 3.375, 0.375),  # G
    (67, 3.75, 0.375),  # F#
    (69, 4.125, 0.375),  # G
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
