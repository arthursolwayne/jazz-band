
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
            note = pretty_midi.Note(velocity=70, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.5 + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=1.875 + 0.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.25 + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=2.625 + 0.375),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.999, end=2.999 + 0.375),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.375 + 0.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=3.75 + 0.375),  # B
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.125 + 0.375),  # C
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.5 + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=4.875 + 0.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=79, start=5.25, end=5.25 + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=5.625 + 0.375),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# D7 on beat 2, G7 on beat 4
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=1.875 + 0.125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=1.875 + 0.125),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=1.875 + 0.125),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=1.875 + 0.125),  # C
    # Bar 3: G7 on beat 4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.375 + 0.125),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.375 + 0.125),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.375 + 0.125),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.375 + 0.125),  # F
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=4.875 + 0.125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=4.875 + 0.125),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=4.875 + 0.125),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=4.875 + 0.125),  # C
]
piano.notes.extend(piano_notes)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.5 + 0.1875),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.6875, end=1.6875 + 0.1875),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=1.875 + 0.1875),  # A
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.25 + 0.1875),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.4375, end=2.4375 + 0.1875),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=2.625 + 0.1875),  # A
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.5 + 0.1875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.6875, end=4.6875 + 0.1875),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=4.875 + 0.1875),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=5.0625, end=5.0625 + 0.1875),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.25 + 0.1875),  # G
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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
            note = pretty_midi.Note(velocity=70, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('jazz_intro.mid')
