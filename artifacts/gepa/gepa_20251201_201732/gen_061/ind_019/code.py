
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, using roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=37, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # F

    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # Gb
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125), # Gb
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # F

    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=80, pitch=37, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),  # Ab
]

# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),  # Db
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Hihat on 1, 2, 3, 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875))
    # Kick on 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))

drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53), Ab (51), Bb (50), F (53)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=50, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.125),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
