
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
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        for eighth in range(2):
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=37, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # A#
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5),  # C#
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.625), # E#
    pretty_midi.Note(velocity=80, pitch=55, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7: F A C Eb
# Bb7: Bb D F Ab
# C7: C E G Bb
# E7: E G# B D
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),  # Eb

    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=54, start=3.0, end=3.375),  # Ab

    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # Bb

    pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.375),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=6.0, end=6.375),  # G#
    pretty_midi.Note(velocity=90, pitch=71, start=6.0, end=6.375),  # B
    pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.375),  # D
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    for beat in range(4):
        time = start + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        for eighth in range(2):
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F - G# - A - F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=56, start=1.75, end=1.875), # G#
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=56, start=3.25, end=3.375), # G#
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=56, start=5.5, end=5.625), # G#
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=5.75), # A
    pretty_midi.Note(velocity=100, pitch=53, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
