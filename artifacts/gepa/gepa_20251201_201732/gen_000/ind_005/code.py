
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
def add_drums(start, duration):
    kick = pretty_midi.Note(velocity=90, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=90, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + duration, step=0.375)
    for t in hihat:
        if t < start + duration:
            hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.375)
            drums.notes.append(hihat_note)
    drums.notes.append(kick)
    drums.notes.append(snare)

add_drums(0.0, 1.5)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
def add_bass(start):
    # D2 (38) -> F2 (41) -> G2 (43) -> Bb2 (45)
    notes = [
        pretty_midi.Note(velocity=80, pitch=38, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=41, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=80, pitch=43, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=45, start=start + 1.125, end=start + 1.5)
    ]
    for note in notes:
        bass.notes.append(note)

add_bass(1.5)

# Diane: Open voicings, different chord each bar, resolve on the last.
def add_piano(start):
    # Bar 2: Dm7 (D F A C)
    chord = [pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.75),
             pretty_midi.Note(velocity=100, pitch=65, start=start, end=start + 0.75),
             pretty_midi.Note(velocity=100, pitch=67, start=start, end=start + 0.75),
             pretty_midi.Note(velocity=100, pitch=69, start=start, end=start + 0.75)]
    for note in chord:
        piano.notes.append(note)

    # Bar 3: Gm7 (G Bb D F)
    chord = [pretty_midi.Note(velocity=100, pitch=67, start=start + 0.75, end=start + 1.5),
             pretty_midi.Note(velocity=100, pitch=70, start=start + 0.75, end=start + 1.5),
             pretty_midi.Note(velocity=100, pitch=72, start=start + 0.75, end=start + 1.5),
             pretty_midi.Note(velocity=100, pitch=74, start=start + 0.75, end=start + 1.5)]
    for note in chord:
        piano.notes.append(note)

    # Bar 4: Cm7 (C Eb G Bb)
    chord = [pretty_midi.Note(velocity=100, pitch=60, start=start + 1.5, end=start + 3.0),
             pretty_midi.Note(velocity=100, pitch=63, start=start + 1.5, end=start + 3.0),
             pretty_midi.Note(velocity=100, pitch=65, start=start + 1.5, end=start + 3.0),
             pretty_midi.Note(velocity=100, pitch=67, start=start + 1.5, end=start + 3.0)]
    for note in chord:
        piano.notes.append(note)

add_piano(1.5)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
def add_sax(start):
    # Motif: D4 (62) -> F4 (65) -> Bb4 (70) -> D5 (72)
    # First pass: D4 to Bb4
    sax_note1 = pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.75)
    sax_note2 = pretty_midi.Note(velocity=100, pitch=70, start=start + 0.75, end=start + 1.125)
    sax.notes.append(sax_note1)
    sax.notes.append(sax_note2)

    # Second pass: F4 to D5
    sax_note3 = pretty_midi.Note(velocity=100, pitch=65, start=start + 1.5, end=start + 2.25)
    sax_note4 = pretty_midi.Note(velocity=100, pitch=72, start=start + 2.25, end=start + 3.0)
    sax.notes.append(sax_note3)
    sax.notes.append(sax_note4)

add_sax(1.5)

# Bar 3: Full quartet (3.0 - 4.5s)
add_drums(3.0, 1.5)
add_bass(3.0)
add_piano(3.0)
# Diane: no new chord, same as before, but sustain
# Dante: no new motif, just sustain Bb4 and D5

# Bar 4: Full quartet (4.5 - 6.0s)
add_drums(4.5, 1.5)
add_bass(4.5)
add_piano(4.5)
# Dante: final note D5 (72), sustained
sax_note5 = pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0)
sax.notes.append(sax_note5)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
