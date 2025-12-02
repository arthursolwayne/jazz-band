
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
    # Hihat on every eighth
    hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repeated notes
for bar in range(2, 5):
    start = bar * 1.5
    # Bass line: Dm7 walking bass line
    if bar == 2:
        bass_notes = [pretty_midi.Note(velocity=90, pitch=62, start=start, end=start + 0.375),  # D
                      pretty_midi.Note(velocity=90, pitch=60, start=start + 0.375, end=start + 0.75),  # C
                      pretty_midi.Note(velocity=90, pitch=63, start=start + 0.75, end=start + 1.125),  # Eb
                      pretty_midi.Note(velocity=90, pitch=62, start=start + 1.125, end=start + 1.5)]  # D
    elif bar == 3:
        bass_notes = [pretty_midi.Note(velocity=90, pitch=62, start=start, end=start + 0.375),  # D
                      pretty_midi.Note(velocity=90, pitch=60, start=start + 0.375, end=start + 0.75),  # C
                      pretty_midi.Note(velocity=90, pitch=63, start=start + 0.75, end=start + 1.125),  # Eb
                      pretty_midi.Note(velocity=90, pitch=62, start=start + 1.125, end=start + 1.5)]  # D
    elif bar == 4:
        bass_notes = [pretty_midi.Note(velocity=90, pitch=62, start=start, end=start + 0.375),  # D
                      pretty_midi.Note(velocity=90, pitch=60, start=start + 0.375, end=start + 0.75),  # C
                      pretty_midi.Note(velocity=90, pitch=63, start=start + 0.75, end=start + 1.125),  # Eb
                      pretty_midi.Note(velocity=90, pitch=65, start=start + 1.125, end=start + 1.5)]  # F
    bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Dm7 on 1, comp on 2 and 4
        piano_notes = [
            pretty_midi.Note(velocity=90, pitch=62, start=start, end=start + 0.375),  # D
            pretty_midi.Note(velocity=90, pitch=67, start=start, end=start + 0.375),  # G
            pretty_midi.Note(velocity=90, pitch=64, start=start, end=start + 0.375),  # Bb
            pretty_midi.Note(velocity=90, pitch=69, start=start, end=start + 0.375),  # C
            pretty_midi.Note(velocity=90, pitch=67, start=start + 0.375, end=start + 0.75),  # G
            pretty_midi.Note(velocity=90, pitch=69, start=start + 0.375, end=start + 0.75),  # C
            pretty_midi.Note(velocity=90, pitch=62, start=start + 1.125, end=start + 1.5),  # D
            pretty_midi.Note(velocity=90, pitch=67, start=start + 1.125, end=start + 1.5),  # G
            pretty_midi.Note(velocity=90, pitch=64, start=start + 1.125, end=start + 1.5),  # Bb
            pretty_midi.Note(velocity=90, pitch=69, start=start + 1.125, end=start + 1.5)   # C
        ]
    elif bar == 3:
        # Dm7 on 1, comp on 2 and 4
        piano_notes = [
            pretty_midi.Note(velocity=90, pitch=62, start=start, end=start + 0.375),  # D
            pretty_midi.Note(velocity=90, pitch=67, start=start, end=start + 0.375),  # G
            pretty_midi.Note(velocity=90, pitch=64, start=start, end=start + 0.375),  # Bb
            pretty_midi.Note(velocity=90, pitch=69, start=start, end=start + 0.375),  # C
            pretty_midi.Note(velocity=90, pitch=67, start=start + 0.375, end=start + 0.75),  # G
            pretty_midi.Note(velocity=90, pitch=69, start=start + 0.375, end=start + 0.75),  # C
            pretty_midi.Note(velocity=90, pitch=62, start=start + 1.125, end=start + 1.5),  # D
            pretty_midi.Note(velocity=90, pitch=67, start=start + 1.125, end=start + 1.5),  # G
            pretty_midi.Note(velocity=90, pitch=64, start=start + 1.125, end=start + 1.5),  # Bb
            pretty_midi.Note(velocity=90, pitch=69, start=start + 1.125, end=start + 1.5)   # C
        ]
    elif bar == 4:
        # Dm7 on 1, comp on 2 and 4
        piano_notes = [
            pretty_midi.Note(velocity=90, pitch=62, start=start, end=start + 0.375),  # D
            pretty_midi.Note(velocity=90, pitch=67, start=start, end=start + 0.375),  # G
            pretty_midi.Note(velocity=90, pitch=64, start=start, end=start + 0.375),  # Bb
            pretty_midi.Note(velocity=90, pitch=69, start=start, end=start + 0.375),  # C
            pretty_midi.Note(velocity=90, pitch=67, start=start + 0.375, end=start + 0.75),  # G
            pretty_midi.Note(velocity=90, pitch=69, start=start + 0.375, end=start + 0.75),  # C
            pretty_midi.Note(velocity=90, pitch=62, start=start + 1.125, end=start + 1.5),  # D
            pretty_midi.Note(velocity=90, pitch=67, start=start + 1.125, end=start + 1.5),  # G
            pretty_midi.Note(velocity=90, pitch=64, start=start + 1.125, end=start + 1.5),  # Bb
            pretty_midi.Note(velocity=90, pitch=69, start=start + 1.125, end=start + 1.5)   # C
        ]
    piano.notes.extend(piano_notes)

# Sax: Motif - start with D, then F#, then Bb, then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),   # F#
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),   # F#
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0)    # F#
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
