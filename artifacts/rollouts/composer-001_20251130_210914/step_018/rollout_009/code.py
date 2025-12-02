
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
for bar in [0]:
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.125)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.125)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# F7 chord: F A C E
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=1.625, end=1.75), # E
    pretty_midi.Note(velocity=80, pitch=70, start=1.75, end=1.875), # F#
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0),  # F

    pretty_midi.Note(velocity=80, pitch=71, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=80, pitch=70, start=2.125, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.375), # G#
    pretty_midi.Note(velocity=80, pitch=71, start=2.375, end=2.5),  # G

    pretty_midi.Note(velocity=80, pitch=72, start=2.5, end=2.625),  # G#
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=2.75), # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=2.875), # F
    pretty_midi.Note(velocity=80, pitch=70, start=2.875, end=3.0),  # F#

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.125),  # F#
    pretty_midi.Note(velocity=80, pitch=71, start=3.125, end=3.25), # G
    pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.375), # G#
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.5),  # G

    pretty_midi.Note(velocity=80, pitch=70, start=3.5, end=3.625),  # F#
    pretty_midi.Note(velocity=80, pitch=72, start=3.625, end=3.75), # G#
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=3.875), # G
    pretty_midi.Note(velocity=80, pitch=70, start=3.875, end=4.0),  # F#

    pretty_midi.Note(velocity=80, pitch=69, start=4.0, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.25), # F#
    pretty_midi.Note(velocity=80, pitch=68, start=4.25, end=4.375), # E
    pretty_midi.Note(velocity=80, pitch=69, start=4.375, end=4.5),  # F

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=4.625, end=4.75), # F#
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=4.875), # G
    pretty_midi.Note(velocity=80, pitch=70, start=4.875, end=5.0),  # F#

    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=80, pitch=71, start=5.125, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.375), # F#
    pretty_midi.Note(velocity=80, pitch=69, start=5.375, end=5.5),  # F

    pretty_midi.Note(velocity=80, pitch=68, start=5.5, end=5.625),  # E
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=5.75), # F
    pretty_midi.Note(velocity=80, pitch=71, start=5.75, end=5.875), # G
    pretty_midi.Note(velocity=80, pitch=69, start=5.875, end=6.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# F7: F A C E
# Comp on 2 and 4
for bar in [1, 2, 3]:
    for beat in [1, 3]:
        for pitch in [69, 71, 72, 76]:  # F, A, C, E
            note = pretty_midi.Note(velocity=80, pitch=pitch, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.125)
            piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [1, 2, 3]:
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.125)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.125)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.125)
        drums.notes.append(note)

# Sax: Short motif, one phrase, leave it hanging, come back and finish it
# F7 scale: F, G, A, Bb, B, C, D, E
# Motif: F, Bb, B, F
# Start it, leave it hanging, come back and finish it

# First phrase: F, Bb, B, F (Bar 2, beats 1-2)
note = pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.625)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=70, start=1.625, end=1.75)  # G
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=1.875)  # A
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0)  # Bb
sax.notes.append(note)

# Leave it hanging
note = pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.125)  # A (hold)
sax.notes.append(note)

# Come back, finish it
note = pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.625)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75)  # Bb
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=71, start=2.75, end=2.875)  # A
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=2.875, end=3.0)  # F
sax.notes.append(note)

# Second phrase: B, C, E, F (Bar 3, beats 2-3)
note = pretty_midi.Note(velocity=110, pitch=71, start=3.125, end=3.25)  # B
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.375)  # C
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=76, start=3.375, end=3.5)  # E
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.625)  # F
sax.notes.append(note)

# F on beat 4 of bar 3
note = pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=3.875)  # F
sax.notes.append(note)

# Final cadence: F, Bb, E, F (Bar 4, beats 1-2)
note = pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.625)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75)  # Bb
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=76, start=4.75, end=4.875)  # E
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0)  # F
sax.notes.append(note)

# Leave it hanging
note = pretty_midi.Note(velocity=110, pitch=71, start=5.0, end=5.125)  # A (hold)
sax.notes.append(note)

# End on F
note = pretty_midi.Note(velocity=110, pitch=69, start=5.5, end=5.625)  # F
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
