
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
drum_notes = []
for beat in [0, 1, 2, 3]:
    time = beat * 0.375
    if beat % 2 == 0:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))
    else:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches, Dm7 -> G7 -> Cm7 -> F7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.625, end=1.75), # C#
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=1.875), # C
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # D

    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=2.125, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.375), # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.375, end=2.5),  # G

    pretty_midi.Note(velocity=90, pitch=57, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=56, start=2.625, end=2.75), # B
    pretty_midi.Note(velocity=90, pitch=55, start=2.75, end=2.875), # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=2.875, end=3.0),  # C

    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=3.125, end=3.25), # C#
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.375), # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.5),  # D

    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.625),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=3.625, end=3.75), # F#
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=3.875), # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.875, end=4.0),  # G

    pretty_midi.Note(velocity=90, pitch=57, start=4.0, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=56, start=4.125, end=4.25), # B
    pretty_midi.Note(velocity=90, pitch=55, start=4.25, end=4.375), # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=4.375, end=4.5),  # C

    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=4.625, end=4.75), # C#
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=4.875), # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0),  # D

    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.125),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=5.125, end=5.25), # F#
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.375), # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.375, end=5.5),  # G

    pretty_midi.Note(velocity=90, pitch=57, start=5.5, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=56, start=5.625, end=5.75), # B
    pretty_midi.Note(velocity=90, pitch=55, start=5.75, end=5.875), # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=5.875, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.75), # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.75),

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=76, start=2.5, end=2.75), # G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=78, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=80, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=81, start=2.5, end=2.75),

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75), # Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.75),

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.75), # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.75),
]
piano.notes.extend(piano_notes)

# Sax: Motif in Dm, one short phrase, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75), # E
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.125, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375), # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.375, end=2.5),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.75), # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.875, end=3.0),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25), # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.625, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.875, end=4.0),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.25), # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.375), # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.375, end=4.5),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75), # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.125, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375), # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.375, end=5.5),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.75), # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=5.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.875, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: fill the bar
for bar in [2, 3, 4]:
    for beat in [0, 1, 2, 3]:
        time = (bar + 0.5) * 1.5 + beat * 0.375
        if beat % 2 == 0:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))
        else:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
