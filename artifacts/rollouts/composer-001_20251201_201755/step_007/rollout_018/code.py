
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
    # Kick on 1 and 3 (0.0, 0.75, 1.5)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.875),
    # Snare on 2 and 4 (0.375, 1.125)
    pretty_midi.Note(velocity=110, pitch=38, start=0.375, end=0.5),
    pretty_midi.Note(velocity=110, pitch=38, start=1.125, end=1.25),
    # Hi-hat on every eighth (0.0, 0.375, 0.75, 1.125)
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 - F (1.5s)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.625),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.625),  # C3
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625),  # B2 (chromatic approach)
    # Bar 3 - Bb (2.25s)
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.375),  # Bb2
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.375),  # F3
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.375),  # E2 (chromatic approach)
    # Bar 4 - C (3.0s)
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.125),  # C2
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.125),  # G3
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.125),  # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano (Diane): open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.75),  # F2
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.75),  # A2
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75),  # C3
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.75),  # E3
]
# Bar 3: Bbmaj7 (Bb D F A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.5),  # Bb2
    pretty_midi.Note(velocity=100, pitch=46, start=2.25, end=2.5),  # D2
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.5),  # F2
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.5),  # A2
])
# Bar 4: Cmaj7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.25),  # C2
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.25),  # E2
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.25),  # G2
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.25),  # B2
])
piano.notes.extend(piano_notes)

# Sax (Dante): one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F Bb D F (sax is transposed, so F is Bb in concert)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # Bb4
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.0),  # A4 (Bb chromatic)
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # C5
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # Bb4 (return)
]
sax.notes.extend(sax_notes)

# Drums: continue with same pattern, 1.5s to 6.0s
for start in [1.5, 2.25, 3.0]:
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.125),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.5),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.25)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + 0.75, end=1.5 + 0.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25 + 0.75, end=2.25 + 0.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0 + 0.75, end=3.0 + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.5 + 0.375, end=1.5 + 0.5),
    pretty_midi.Note(velocity=110, pitch=38, start=1.5 + 1.125, end=1.5 + 1.25),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25 + 0.375, end=2.25 + 0.5),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25 + 1.125, end=2.25 + 1.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0 + 0.375, end=3.0 + 0.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0 + 1.125, end=3.0 + 1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + 0.375, end=1.5 + 0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + 0.75, end=1.5 + 0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + 1.125, end=1.5 + 1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25 + 0.375, end=2.25 + 0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25 + 0.75, end=2.25 + 0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25 + 1.125, end=2.25 + 1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0 + 0.375, end=3.0 + 0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0 + 0.75, end=3.0 + 0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0 + 1.125, end=3.0 + 1.25)
])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
