
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.extend([kick1, kick2])
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([snare1, snare2])
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Sax: short motif, start it, leave it hanging, come back and finish it
# D7 chord: D F# A C#
# Motif: D - F# - B - D (with slight chromaticism)

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),    # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),   # F#
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),    # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.125, end=2.25),   # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),    # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25),   # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),    # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=3.75),   # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),    # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),   # F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),    # B
    pretty_midi.Note(velocity=100, pitch=62, start=5.125, end=5.25)    # D
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),    # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=2.0),     # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),     # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),     # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),     # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),     # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),     # B
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),     # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),     # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.0),     # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),     # E
    pretty_midi.Note(velocity=90, pitch=65, start=4.25, end=4.5),     # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),     # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),     # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.25),     # B
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.5),     # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),    # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),    # F#
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),    # C#
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),    # B
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),    # D
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),    # F#
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.5),    # A
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),    # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),    # F#
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),    # C#
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),    # B
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=5.0),    # D
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=5.0),    # F#
    pretty_midi.Note(velocity=90, pitch=76, start=4.75, end=5.0),    # A
]
piano.notes.extend(piano_notes)

# Drums: same pattern as bar 1, repeated for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.extend([kick1, kick2])
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([snare1, snare2])
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
