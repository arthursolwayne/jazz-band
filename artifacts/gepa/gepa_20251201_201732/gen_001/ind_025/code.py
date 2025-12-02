
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
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

# Bars 2-4: Full quartet

# Bass line (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # F2 on 2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2 on 3
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2 on 4
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2 on 1
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75), # F2 on 2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125), # G2 on 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2 on 4
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2 on 1
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25), # F2 on 2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # G2 on 3
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # D2 on 4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
]

# Bar 3: G7 (G-B-D-F)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F5 (chromatic)
]

# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # Bb4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - Eb4 - D4 (start), then F4 - Eb4 - D4 (finish)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=1.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D4 (hanging)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.75),  # F4
    pretty_midi.Note(velocity=100, pitch=63, start=2.75, end=2.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=3.0),  # D4 (resolve)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25),

    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.875, end=bar_start + 2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 2.25, end=bar_start + 2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 2.625, end=bar_start + 3.0),

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
