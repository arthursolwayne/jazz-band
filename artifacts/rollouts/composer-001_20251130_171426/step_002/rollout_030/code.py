
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, kick2, snare, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=54, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=56, start=4.125, end=4.5),  # C#
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
# Bar 2: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
]
piano.notes.extend(piano_notes)

# Sax (Dante): Melody - short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=110, pitch=58, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=58, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Drums again for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, kick2, snare, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
