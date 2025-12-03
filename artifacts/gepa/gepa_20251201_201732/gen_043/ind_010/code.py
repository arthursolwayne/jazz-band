
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
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, kick2, snare, snare2, hihat, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2 (1.5 - 3.0s)
# Bass: F (D2), G (E2), A (F2), Bb (G2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # Ab
]
piano.notes.extend(piano_notes)

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F (1.5 - 2.25s), then rest until 5.25s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, kick2, snare, snare2, hihat, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
