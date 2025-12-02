
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
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i*0.375, end=start + i*0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=58, start=4.125, end=4.5),   # C#
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7 on 2, Bb7 on 4
# F7: F, A, C, Eb
# Bb7: Bb, D, F, Ab
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=71, start=1.875, end=2.25),  # A (F7)
    pretty_midi.Note(velocity=85, pitch=72, start=1.875, end=2.25),  # Bb (F7)
    pretty_midi.Note(velocity=85, pitch=74, start=1.875, end=2.25),  # C (F7)
    pretty_midi.Note(velocity=85, pitch=76, start=1.875, end=2.25),  # Eb (F7)
    pretty_midi.Note(velocity=85, pitch=73, start=3.375, end=3.75),  # D (Bb7)
    pretty_midi.Note(velocity=85, pitch=76, start=3.375, end=3.75),  # F (Bb7)
    pretty_midi.Note(velocity=85, pitch=78, start=3.375, end=3.75),  # G (Bb7)
    pretty_midi.Note(velocity=85, pitch=80, start=3.375, end=3.75),  # Ab (Bb7)
]
piano.notes.extend(piano_notes)

# Drums: continue same pattern for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i*0.375, end=start + i*0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, G#, Bb, F (melodic motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=1.875, end=2.25),  # G#
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=100, pitch=73, start=3.375, end=3.75),  # G#
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
