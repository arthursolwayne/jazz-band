
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

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
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus) - Walking line, chromatic approach to Fm
bass_notes = [
    # Bar 2: F - Gb - E - D
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=1.875),   # F (41)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # Gb (40)
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625),  # E (40 - chromatic approach)
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),   # D (40 - chromatic approach)
    # Bar 3: C - Bb - A - G
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # C (36)
    pretty_midi.Note(velocity=100, pitch=37, start=3.375, end=3.75),  # Bb (37)
    pretty_midi.Note(velocity=100, pitch=37, start=3.75, end=4.125),  # A (37 - chromatic)
    pretty_midi.Note(velocity=100, pitch=37, start=4.125, end=4.5),   # G (37 - chromatic)
    # Bar 4: F - Ab - G - Eb
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875),   # F (41)
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # Ab (40)
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625),  # G (40 - chromatic)
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),   # Eb (40 - chromatic)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
# Bar 2: F7 on 2 and 4
piano_notes = [
    # Bar 2 - F7 on beat 2 and 4
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),   # F
    pretty_midi.Note(velocity=100, pitch=46, start=1.875, end=2.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25),   # E
    pretty_midi.Note(velocity=100, pitch=47, start=1.875, end=2.25),   # Ab
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75),   # E
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75),   # Ab
    # Bar 3 - F7 on beat 2 and 4
    pretty_midi.Note(velocity=100, pitch=41, start=3.875, end=4.25),   # F
    pretty_midi.Note(velocity=100, pitch=46, start=3.875, end=4.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=44, start=3.875, end=4.25),   # E
    pretty_midi.Note(velocity=100, pitch=47, start=3.875, end=4.25),   # Ab
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),   # F
    pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25),   # E
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.25),   # Ab
]
piano.notes.extend(piano_notes)

# Drums (Little Ray) - Same pattern as Bar 1, repeated in Bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Sax (Dante) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (41) - Bb (46) - F (41) - Eb (40)
# Bar 2: Start motif on beat 1
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=41, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=110, pitch=46, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=41, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=40, start=2.625, end=3.0),   # Eb
    # Bar 3: Repeat motif on beat 1
    pretty_midi.Note(velocity=110, pitch=41, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=110, pitch=46, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=41, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=110, pitch=40, start=4.125, end=4.5),   # Eb
    # Bar 4: Start motif on beat 1, finish it on beat 4
    pretty_midi.Note(velocity=110, pitch=41, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=110, pitch=46, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=41, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=40, start=5.625, end=6.0),   # Eb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
