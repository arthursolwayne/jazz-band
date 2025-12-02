
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=39, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=41, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=100, pitch=44, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=100, pitch=46, start=2.375, end=2.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=47, start=2.5, end=2.625),  # C#
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=2.75, end=2.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=2.875, end=3.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.75),  # B (Fm7: F Ab Bb B)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Motif - short, singable, leave it hanging
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # A
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # A
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),  # A
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3])
# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.extend([snare2, snare4])
# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
