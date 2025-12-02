
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass (Marcus): Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),   # D2
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625),  # A2 (fifth of Dm)
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),   # G2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar
piano_notes = [
    # Bar 2: Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # C5

    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # F4 (chromatic approach)

    # Bar 4: Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.75),  # Bb4
]
piano.notes.extend(piano_notes)

# Drums (Bar 2): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i*1.5, end=1.5 + i*1.5 + 0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875 + i*1.5, end=1.875 + i*1.5 + 0.375),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + i*1.5, end=1.5 + i*1.5 + 0.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=1.875 + i*1.5, end=1.875 + i*1.5 + 0.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=2.25 + i*1.5, end=2.25 + i*1.5 + 0.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=2.625 + i*1.5, end=2.625 + i*1.5 + 0.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=2.625 + i*1.5, end=2.625 + i*1.5 + 0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.0 + i*1.5, end=3.0 + i*1.5 + 0.375),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.0 + i*1.5, end=3.0 + i*1.5 + 0.375),  # Hihat

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
])

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62) -> F4 (65) -> A4 (69) -> D5 (72) (but leave it hanging on A4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A4 again
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),   # D5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
