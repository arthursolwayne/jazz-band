
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
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625)),
    (pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75)),
    (pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=1.875)),
    (pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0)),
    # Bar 3
    (pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125)),
    (pretty_midi.Note(velocity=100, pitch=68, start=2.125, end=2.25)),
    (pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.375)),
    (pretty_midi.Note(velocity=100, pitch=70, start=2.375, end=2.5)),
    # Bar 4
    (pretty_midi.Note(velocity=100, pitch=70, start=2.5, end=2.625)),
    (pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.75)),
    (pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=2.875)),
    (pretty_midi.Note(velocity=100, pitch=73, start=2.875, end=3.0)),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 (F7) on beat 2
    (pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875)),  # F
    (pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=1.875)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=77, start=1.75, end=1.875)),  # C
    (pretty_midi.Note(velocity=100, pitch=80, start=1.75, end=1.875)),  # E
    # Bar 3: C7 (F7) on beat 2
    (pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.375)),  # F
    (pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.375)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.375)),  # C
    (pretty_midi.Note(velocity=100, pitch=80, start=2.25, end=2.375)),  # E
    # Bar 4: C7 (F7) on beat 2
    (pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=2.875)),  # F
    (pretty_midi.Note(velocity=100, pitch=76, start=2.75, end=2.875)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=77, start=2.75, end=2.875)),  # C
    (pretty_midi.Note(velocity=100, pitch=80, start=2.75, end=2.875)),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start of motif
    (pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75)),  # G
    # Bar 3: Continue motif
    (pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25)),  # A
    # Bar 4: Finish motif
    (pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.75)),  # B
    (pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0)),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
