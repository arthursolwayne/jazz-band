
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0, resolution=120)]
midi.tempo_changes = [pretty_midi.TempoChange(tempo=120, time=0.0)]

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=beat * 0.375 + 0.125)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=beat * 0.375 + 0.125)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375, end=beat * 0.375 + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=1.625, end=1.75),  # C#
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.0),  # D#
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.125, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.375),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.375, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=2.5, end=2.625),  # G#
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=2.75, end=2.875),  # A#
    pretty_midi.Note(velocity=90, pitch=71, start=2.875, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=3.125, end=3.25),  # C#
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=75, start=3.375, end=3.5),  # D#
    pretty_midi.Note(velocity=90, pitch=76, start=3.5, end=3.625),  # E
    pretty_midi.Note(velocity=90, pitch=77, start=3.625, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=78, start=3.75, end=3.875),  # F#
    pretty_midi.Note(velocity=90, pitch=79, start=3.875, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=80, start=4.0, end=4.125),  # G#
    pretty_midi.Note(velocity=90, pitch=81, start=4.125, end=4.25),  # A
    pretty_midi.Note(velocity=90, pitch=82, start=4.25, end=4.375),  # A#
    pretty_midi.Note(velocity=90, pitch=83, start=4.375, end=4.5),  # B
    pretty_midi.Note(velocity=90, pitch=84, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=90, pitch=85, start=4.625, end=4.75),  # C#
    pretty_midi.Note(velocity=90, pitch=86, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=87, start=4.875, end=5.0),  # D#
    pretty_midi.Note(velocity=90, pitch=88, start=5.0, end=5.125),  # E
    pretty_midi.Note(velocity=90, pitch=89, start=5.125, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=90, start=5.25, end=5.375),  # F#
    pretty_midi.Note(velocity=90, pitch=91, start=5.375, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=92, start=5.5, end=5.625),  # G#
    pretty_midi.Note(velocity=90, pitch=93, start=5.625, end=5.75),  # A
    pretty_midi.Note(velocity=90, pitch=94, start=5.75, end=5.875),  # A#
    pretty_midi.Note(velocity=90, pitch=95, start=5.875, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: C7 on beat 2
note = pretty_midi.Note(velocity=100, pitch=60, start=1.625, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.625, end=1.75)
piano.notes.append(note)

# Bar 3: C7 on beat 2
note = pretty_midi.Note(velocity=100, pitch=60, start=3.125, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.125, end=3.25)
piano.notes.append(note)

# Bar 4: C7 on beat 2
note = pretty_midi.Note(velocity=100, pitch=60, start=4.625, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=4.625, end=4.75)
piano.notes.append(note)

# Sax: Melody - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C E B (bar 2), G E D (bar 3), C E B (bar 4)
# Bar 2
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.625)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.625)
sax.notes.append(note)

# Bar 3
note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125)
sax.notes.append(note)

# Bar 4
note = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.625)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625)
sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=(bar * 1.5) + beat * 0.375, end=(bar * 1.5) + beat * 0.375 + 0.125)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=(bar * 1.5) + beat * 0.375, end=(bar * 1.5) + beat * 0.375 + 0.125)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=(bar * 1.5) + beat * 0.375, end=(bar * 1.5) + beat * 0.375 + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
