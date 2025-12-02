
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in D, chromatic approach to G
bass_notes = [
    (pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625)),   # D
    (pretty_midi.Note(velocity=90, pitch=64, start=1.625, end=1.75)),  # Eb
    (pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=1.875)),  # E
    (pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0)),   # G
    (pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125)),   # A
    (pretty_midi.Note(velocity=90, pitch=71, start=2.125, end=2.25)),  # B
    (pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.375)),  # C
    (pretty_midi.Note(velocity=90, pitch=74, start=2.375, end=2.5)),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on Dmaj7
piano_notes = [
    # Bar 2: Dmaj7 (2nd beat)
    pretty_midi.Note(velocity=100, pitch=62, start=1.625, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=1.625, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.625, end=1.875),  # D
    # Bar 3: Bm7 (4th beat)
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.125),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=2.875, end=3.125),  # F#
    pretty_midi.Note(velocity=100, pitch=76, start=2.875, end=3.125),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=2.875, end=3.125),  # D
]
piano.notes.extend(piano_notes)

# Sax: Motif in D minor, starts on beat 1, ends on beat 3
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.125),  # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.25), # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.375), # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.375, end=2.5),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Drums
for i in range(4):
    time = 1.5 + i * 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125))

# Bar 4: Full quartet
# Bass: Walking line in D, chromatic approach to G
bass_notes = [
    (pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125)),   # D
    (pretty_midi.Note(velocity=90, pitch=64, start=3.125, end=3.25)),  # Eb
    (pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.375)),  # E
    (pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5)),   # G
    (pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.625)),   # A
    (pretty_midi.Note(velocity=90, pitch=71, start=3.625, end=3.75)),  # B
    (pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=3.875)),  # C
    (pretty_midi.Note(velocity=90, pitch=74, start=3.875, end=4.0)),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on Dmaj7
piano_notes = [
    # Bar 4: Dmaj7 (2nd beat)
    pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=3.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.875),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.625, end=3.875),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.625, end=3.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: Motif variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.375),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5),   # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.625),  # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.75), # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=3.875), # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.875, end=4.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 4: Drums
for i in range(4):
    time = 3.0 + i * 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
