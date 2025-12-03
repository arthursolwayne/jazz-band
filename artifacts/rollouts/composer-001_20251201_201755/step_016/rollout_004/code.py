
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
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=110, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=60, pitch=42, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # Fm root (F)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # Bb (Fm 3rd)
    pretty_midi.Note(velocity=80, pitch=39, start=2.25, end=2.625), # Ab (Fm b7)
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # C (Fm 5th)

    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # Gb (Fm b3)
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75), # A (Fm 7)
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.125), # Bb (Fm 3rd)
    pretty_midi.Note(velocity=80, pitch=39, start=4.125, end=4.5),  # Ab (Fm b7)

    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # Bb (3rd)
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # Gb (b3)
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0),  # C (5th)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),  # Eb

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=4.5),  # Ab

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=6.0),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53) - Ab (51) - C (55) - Bb (50), then leave it hanging on the last note
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=50, start=2.625, end=3.0),  # Bb

    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=4.125, end=4.5),  # C

    # Come back and finish it
    pretty_midi.Note(velocity=110, pitch=50, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=5.625, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=(1.5 + beat * 0.375), end=(1.5 + (beat + 1) * 0.375))
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=110, pitch=38, start=(1.5 + beat * 0.375), end=(1.5 + (beat + 1) * 0.375))
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=60, pitch=42, start=(1.5 + beat * 0.375), end=(1.5 + (beat + 1) * 0.375))
    drums.notes.append(note)

# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=(3.0 + beat * 0.375), end=(3.0 + (beat + 1) * 0.375))
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=110, pitch=38, start=(3.0 + beat * 0.375), end=(3.0 + (beat + 1) * 0.375))
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=60, pitch=42, start=(3.0 + beat * 0.375), end=(3.0 + (beat + 1) * 0.375))
    drums.notes.append(note)

# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=(4.5 + beat * 0.375), end=(4.5 + (beat + 1) * 0.375))
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=110, pitch=38, start=(4.5 + beat * 0.375), end=(4.5 + (beat + 1) * 0.375))
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=60, pitch=42, start=(4.5 + beat * 0.375), end=(4.5 + (beat + 1) * 0.375))
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
