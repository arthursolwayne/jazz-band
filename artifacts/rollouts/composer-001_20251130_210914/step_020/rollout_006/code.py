
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
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat_1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: D7 chord (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),
    # Bar 3, beat 2: G7 chord (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),
    # Bar 4, beat 2: C7 chord (C, E, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Motif: D (62) -> F# (67) -> G (67) -> D (62)
# Bar 2: Start motif
note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625)
note2 = pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75)
note3 = pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875)
note4 = pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0)
# Bar 4: Finish motif
note5 = pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625)
note6 = pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75)
note7 = pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875)
note8 = pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0)
sax.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat_1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
