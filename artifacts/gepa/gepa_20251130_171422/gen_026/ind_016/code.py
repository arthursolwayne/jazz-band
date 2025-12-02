
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
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=60, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=60, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=60, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=60, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F minor, chromatic approaches
# Fm: F, Ab, Bb, D, Eb, G, A, C
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Fm7 -> Abmaj7 -> Bb7 -> Ebmaj7
        notes = [pretty_midi.Note(velocity=80, pitch=72, start=start, end=start + 0.375),  # F
                 pretty_midi.Note(velocity=80, pitch=69, start=start + 0.375, end=start + 0.75),  # Ab
                 pretty_midi.Note(velocity=80, pitch=68, start=start + 0.75, end=start + 1.125),  # Bb
                 pretty_midi.Note(velocity=80, pitch=66, start=start + 1.125, end=start + 1.5)]  # Eb
    elif bar == 3:
        # D7 -> Abmaj7 -> G7 -> Ebmaj7
        notes = [pretty_midi.Note(velocity=80, pitch=67, start=start, end=start + 0.375),  # D
                 pretty_midi.Note(velocity=80, pitch=69, start=start + 0.375, end=start + 0.75),  # Ab
                 pretty_midi.Note(velocity=80, pitch=68, start=start + 0.75, end=start + 1.125),  # G
                 pretty_midi.Note(velocity=80, pitch=66, start=start + 1.125, end=start + 1.5)]  # Eb
    elif bar == 4:
        # C7 -> Abmaj7 -> Bb7 -> F7
        notes = [pretty_midi.Note(velocity=80, pitch=61, start=start, end=start + 0.375),  # C
                 pretty_midi.Note(velocity=80, pitch=69, start=start + 0.375, end=start + 0.75),  # Ab
                 pretty_midi.Note(velocity=80, pitch=68, start=start + 0.75, end=start + 1.125),  # Bb
                 pretty_midi.Note(velocity=80, pitch=72, start=start + 1.125, end=start + 1.5)]  # F
    bass.notes.extend(notes)

# Piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Fm7
        notes = [pretty_midi.Note(velocity=85, pitch=69, start=start, end=start + 0.375),  # Ab
                 pretty_midi.Note(velocity=85, pitch=72, start=start, end=start + 0.375),  # F
                 pretty_midi.Note(velocity=85, pitch=68, start=start, end=start + 0.375),  # Bb
                 pretty_midi.Note(velocity=85, pitch=76, start=start, end=start + 0.375)]  # D
    elif bar == 3:
        # Abmaj7
        notes = [pretty_midi.Note(velocity=85, pitch=72, start=start, end=start + 0.375),  # F
                 pretty_midi.Note(velocity=85, pitch=74, start=start, end=start + 0.375),  # G
                 pretty_midi.Note(velocity=85, pitch=77, start=start, end=start + 0.375),  # Bb
                 pretty_midi.Note(velocity=85, pitch=79, start=start, end=start + 0.375)]  # C
    elif bar == 4:
        # Ebmaj7
        notes = [pretty_midi.Note(velocity=85, pitch=66, start=start, end=start + 0.375),  # Eb
                 pretty_midi.Note(velocity=85, pitch=69, start=start, end=start + 0.375),  # G
                 pretty_midi.Note(velocity=85, pitch=72, start=start, end=start + 0.375),  # Bb
                 pretty_midi.Note(velocity=85, pitch=74, start=start, end=start + 0.375)]  # D
    piano.notes.extend(notes)

# Sax: Motif with tension and space, make it sing
# First bar is silence, bar 2 starts the motif
# Motif: F, Ab, Bb, Eb (Fm scale)
start = 1.5
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=start, end=start + 0.375),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=start + 0.75, end=start + 1.125),  # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=start + 1.125, end=start + 1.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: continuation or resolution
start = 3.0
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=start, end=start + 0.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=72, start=start + 0.375, end=start + 0.75),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=start + 0.75, end=start + 1.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=68, start=start + 1.125, end=start + 1.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: pause and resolve
start = 4.5
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=start, end=start + 0.375),  # Eb
    pretty_midi.Note(velocity=110, pitch=72, start=start + 0.375, end=start + 0.75),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=start + 0.75, end=start + 1.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=68, start=start + 1.125, end=start + 1.5),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: continue for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=60, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=60, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=60, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=60, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
