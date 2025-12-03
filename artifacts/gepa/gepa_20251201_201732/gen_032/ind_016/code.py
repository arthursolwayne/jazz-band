
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25), # F2 (third)
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.625), # C2 (fifth)
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # Eb2 (chromatic)
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F2 (third)
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125), # G2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),  # A2 (fifth)
    
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25), # F2 (third)
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),  # D#2 (chromatic)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # C5
    
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # F5
    
    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.25),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=5.25),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=5.25),  # Bb4
]
for note in piano_notes:
    piano.notes.append(note)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.75), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75),
]
for note in drum_notes:
    drums.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Motif: D4 - Eb4 - F4 - G4 (Dm), then repeat an octave higher, then resolve on G4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G4

    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.75),  # D5
    pretty_midi.Note(velocity=100, pitch=75, start=2.75, end=3.0),  # Eb5
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.25),  # F5
    pretty_midi.Note(velocity=100, pitch=79, start=3.25, end=3.5),  # G5

    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),  # G4 (resolve)
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
