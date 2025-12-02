
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
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hats on every eighth
    hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Add notes to drums
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=39, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # Gb
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Bar 2
piano_notes = [
    # Bar 2: Fm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),  # F
    # Bar 3: no piano
    # Bar 4: Fm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=39, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25),  # F
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hats on every eighth
    hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Add notes to drums
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

# Sax: Your motif
# Bar 2: Start of motif (F, Ab, Bb, E)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=41, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=42, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=45, start=2.625, end=3.0),  # E
    # Bar 3: Leave it hanging (rest)
    # Bar 4: Return with variation (F, Ab, G, E)
    pretty_midi.Note(velocity=110, pitch=43, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=41, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=44, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=45, start=5.625, end=6.0),  # E
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
