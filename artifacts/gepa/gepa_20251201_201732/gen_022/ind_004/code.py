
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F, Ab, D, C)
# Bar 2: F, Ab, D, C
# Bar 3: Bb, Eb, A, G
# Bar 4: F, Ab, D, C

# Convert to MIDI notes
def note_to_midi(note, octave):
    return pretty_midi.note_number_to_midi(pretty_midi.note_name_to_number(note) + octave * 12)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=note_to_midi('F', 2), start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=note_to_midi('Ab', 2), start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=note_to_midi('D', 2), start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=note_to_midi('C', 2), start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=note_to_midi('Bb', 2), start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=note_to_midi('Eb', 2), start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=note_to_midi('A', 2), start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=note_to_midi('G', 2), start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=note_to_midi('F', 2), start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=note_to_midi('Ab', 2), start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=note_to_midi('D', 2), start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=note_to_midi('C', 2), start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, one chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Fm7 (F, Ab, C, Eb)

def chord_to_notes(chord, octave):
    notes = []
    for note in chord.split():
        pitch = note_to_midi(note, octave)
        notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start, end=bar_end))
    return notes

# Bar 2: Fm7 on beat 2
bar_start = 1.5
bar_end = 3.0
piano.notes.extend(chord_to_notes("F Ab C Eb", 3))

# Bar 3: Bb7 on beat 2
bar_start = 3.0
bar_end = 4.5
piano.notes.extend(chord_to_notes("Bb D F Ab", 3))

# Bar 4: Fm7 on beat 2
bar_start = 4.5
bar_end = 6.0
piano.notes.extend(chord_to_notes("F Ab C Eb", 3))

# Dante: Sax melody
# One short motif, start it, leave it hanging, come back and finish it

# Bar 2: Start the motif
# F (Ab), Bb (C), Ab (Bb), F
# Use Fm scale: F, Ab, Bb, C, Db, Eb, F
note_durations = 0.375
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=note_to_midi('F', 3), start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=note_to_midi('Ab', 3), start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=note_to_midi('Bb', 3), start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=note_to_midi('C', 3), start=2.625, end=3.0),
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=note_to_midi('Ab', 3), start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=note_to_midi('Bb', 3), start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=note_to_midi('F', 3), start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=note_to_midi('C', 3), start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=note_to_midi('Db', 3), start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=note_to_midi('F', 3), start=5.25, end=5.625)
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('jazz_intro.mid')
