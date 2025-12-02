
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
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            notes = [pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)]
            drums.notes.extend(notes)
        if beat == 1 or beat == 3:
            notes = [pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)]
            drums.notes.extend(notes)
        notes = [pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)]
        drums.notes.extend(notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=90, pitch=46, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.5),  # G#
    pretty_midi.Note(velocity=90, pitch=48, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=90, pitch=49, start=2.75, end=3.0),  # A#
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=52, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.0),  # C#
    pretty_midi.Note(velocity=90, pitch=54, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=4.25, end=4.5),  # D#
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=90, pitch=57, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.75),  # G#
    pretty_midi.Note(velocity=90, pitch=61, start=5.75, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7 = F, A, C, E♭
# B♭7 = B♭, D, F, A♭
# C7 = C, E, G, B♭
# E7 = E, G#, B, D
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.75),  # G#
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25),  # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # G#
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # C
]
piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging, come back and finish it
# F, G#, Bb, F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=110, pitch=55, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=110, pitch=57, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=59, start=2.25, end=2.5),  # A
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=53, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=55, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=110, pitch=57, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=110, pitch=59, start=4.25, end=4.5),  # A
    # Finish it
    pretty_midi.Note(velocity=110, pitch=53, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=110, pitch=55, start=5.75, end=6.0),  # E
]
sax.notes.extend(sax_notes)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            notes = [pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)]
            drums.notes.extend(notes)
        if beat == 1 or beat == 3:
            notes = [pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)]
            drums.notes.extend(notes)
        notes = [pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)]
        drums.notes.extend(notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
