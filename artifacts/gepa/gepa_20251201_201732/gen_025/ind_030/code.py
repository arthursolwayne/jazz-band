
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0), # D2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375), # G2
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75), # B2
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125), # A2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5), # G2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.875), # B2
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # D3
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.625), # C#3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=46, start=5.625, end=6.0), # B2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875), # C#4

    # Bar 3: Em7 (E-G-B-D)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # E4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.375), # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # D4

    # Bar 4: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # F4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Bb4 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0), # A4 (resolve)

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5), # A4

    # Bar 4: Return and finish it
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # D4
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25), # A4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0), # A4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2 (1.5 - 3.0s)
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes_bar2:
    drums.notes.append(note)

# Drums: Bar 3 (3.0 - 4.5s)
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes_bar3:
    drums.notes.append(note)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes_bar4:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
