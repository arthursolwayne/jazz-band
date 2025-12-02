
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody - F# G A Bb (F# is the first note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=3.0),   # Bb
]

# Bass: Walking line in F
# F - G - Ab - A - Bb - B - C - D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),   # G
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625),   # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),    # A
]

# Piano: 7th chords on 2 and 4
# F7 on beat 2, Bb7 on beat 4
piano_notes = [
    # F7 (F A C Eb) on beat 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=58, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=2.25),
    # Bb7 (Bb D F Ab) on beat 4 (2.625 - 3.0)
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),
]

sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif but with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=61, start=4.125, end=4.5),   # Bb
]

# Bass: Walking line in F
# Bb - B - C - D - Eb - E - F - G
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75),   # B
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),   # C
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),    # D
]

# Piano: 7th chords on 2 and 4
# Bb7 on beat 2, F7 on beat 4
piano_notes = [
    # Bb7 (Bb D F Ab) on beat 2 (3.375 - 3.75)
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75),
    # F7 (F A C Eb) on beat 4 (4.125 - 4.5)
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=58, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),
]

sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat the motif again, but with a slight resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=6.0),   # Bb
]

# Bass: Walking line in F
# F - G - Ab - A - Bb - B - C - D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),   # G
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625),   # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0),    # A
]

# Piano: 7th chords on 2 and 4
# F7 on beat 2, Bb7 on beat 4
piano_notes = [
    # F7 (F A C Eb) on beat 2 (4.875 - 5.25)
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=58, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25),
    # Bb7 (Bb D F Ab) on beat 4 (5.625 - 6.0)
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),
]

sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

# Add the drum pattern again for bars 3 and 4
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
    drums.notes.append(note)

for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
