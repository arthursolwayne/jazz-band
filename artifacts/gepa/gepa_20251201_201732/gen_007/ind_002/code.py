
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, roots and fifths with chromatic approaches
# Fm: F, Ab, D, C, E, Gb, Bb
# Bar 2: F (root), Gb (chromatic approach), Ab (fifth), Ab (fifth)
# Bar 3: D (fifth), E (chromatic), C (root), C (root)
# Bar 4: Bb (fifth), A (chromatic), F (root), F (root)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),   # Ab

    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5),   # C

    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Dm7b5 (D, F, Ab, C)
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=3.0),  # Eb

    # Bar 3: Bb7
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=56, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=4.5),  # Ab

    # Bar 4: Dm7b5
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=6.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, D, F (target note F, leave on the third beat)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75),  # F (come back)
]
sax.notes.extend(sax_notes)

# Drums: continue the pattern
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 6):
    start = i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25),
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fmintrous.mid")
