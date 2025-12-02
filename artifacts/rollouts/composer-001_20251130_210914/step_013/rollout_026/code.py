
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
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=49, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=47, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=51, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=50, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=49, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=47, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=51, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=50, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=49, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=47, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=51, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=50, start=5.75, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # Db
    pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # Db
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5),  # F

    # Bar 3: Fm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # Db
    pretty_midi.Note(velocity=100, pitch=76, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # Db
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.0),  # F

    # Bar 4: Fm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # Db
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # Db
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.5),  # F
]
piano.notes.extend(piano_notes)

# Drums: fill the bar
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.5),  # Db
    pretty_midi.Note(velocity=110, pitch=66, start=5.75, end=6.0),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
