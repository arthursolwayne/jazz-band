
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

# Kicks on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([drum_kick_1, drum_kick_3])

# Snares on 2 and 4
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.extend([drum_snare_2, drum_snare_4])

# Hi-hats on every eighth note
hihat_start = 0.0
for i in range(8):
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.375)
    drums.notes.append(hihat)
    hihat_start += 0.375

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
# D minor blues scale: D, Eb, F, Gb, G, A, Bb
# Walking bass line: D -> Eb -> F -> Gb (bar 2), G -> A -> Bb -> C (bar 3), D -> Eb -> F -> G (bar 4)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=2.5),  # Gb

    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.5),  # C

    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# D7, F7, G7, A7 (bar 2), Bb7, D7, F7, G7 (bar 3), A7, D7, F7, G7 (bar 4)
# Chord voicings: D7 = D, F#, A, C; F7 = F, A, C, Eb; etc.
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.75),  # F#
    pretty_midi.Note(velocity=85, pitch=74, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.75),  # C

    pretty_midi.Note(velocity=85, pitch=65, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=85, pitch=72, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.5),  # Eb

    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=85, pitch=74, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=85, pitch=72, start=3.0, end=3.25),  # F

    pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=85, pitch=74, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=85, pitch=72, start=3.75, end=4.0),  # Bb

    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=85, pitch=74, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.75),  # C

    pretty_midi.Note(velocity=85, pitch=65, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=85, pitch=72, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.5),  # Eb

    pretty_midi.Note(velocity=85, pitch=67, start=6.0, end=6.25),  # G
    pretty_midi.Note(velocity=85, pitch=74, start=6.0, end=6.25),  # B
    pretty_midi.Note(velocity=85, pitch=69, start=6.0, end=6.25),  # D
    pretty_midi.Note(velocity=85, pitch=72, start=6.0, end=6.25),  # F
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, short motif, one phrase with space
# Motif: D -> Eb -> F -> Gb (bar 2), G -> A -> Bb -> C (bar 3), D -> Eb -> F -> G (bar 4)

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0),  # Gb

    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.875, end=3.0),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),  # G
]
sax.notes.extend(sax_notes)

# Drums continue with the same pattern for bars 2-4
hihat_start = 1.5
for i in range(8):
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.375)
    drums.notes.append(hihat)
    hihat_start += 0.375

# Kicks on 1 and 3
drum_kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875)
drum_kick_4 = pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875)
drums.notes.extend([drum_kick_2, drum_kick_3, drum_kick_4])

# Snares on 2 and 4
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
drum_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5)
drums.notes.extend([drum_snare_2, drum_snare_4])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_4bar_intro.mid")
