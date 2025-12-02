
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line, chromatic approaches
# Dm7 = D F A C
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.6875, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.0625),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.0625, end=2.25),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.4375),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.4375, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=2.625, end=2.8125),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.8125, end=3.0),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.1875, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.5625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.5625, end=3.75),  # F
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Bar 2: comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=95, pitch=64, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.1875),  # C
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bars 2-4 (1.5-6.0)
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.1875, end=bar_start + i * 0.1875 + 0.1875)
        drums.notes.append(hihat)
    # Add kicks and snares
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 = D F A C
# Motif: D (62) -> F (67) -> Bb (66) -> D (62), then D (62) -> A (71) -> C (64) -> D (62)
# Bar 2: D, F, Bb, D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.0625),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.0625, end=2.25),  # D
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.4375),  # D
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=3.1875, end=3.375),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5625),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.5625, end=3.75),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
