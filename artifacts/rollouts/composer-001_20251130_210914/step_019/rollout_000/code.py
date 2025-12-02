
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice.
# Dm7 chord: D F A C
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=100, pitch=61, start=1.6875, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.0625), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25), # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375), # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.4375, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=2.8125), # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.8125, end=3.0), # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875), # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75), # D
    # Bar 4 (continuation)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=3.9375), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.9375, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=61, start=4.125, end=4.3125), # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.3125, end=4.5), # D
    # Bar 4 (end)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875), # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.6875, end=4.875), # Eb
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.0625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.4375), # D
    pretty_midi.Note(velocity=100, pitch=61, start=5.4375, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=5.8125), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.8125, end=6.0), # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
# Dm7 = D F A C
piano_notes = []

# Bar 2
piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875)) # D
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875)) # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.6875)) # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.6875)) # C

# Bar 3
piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375)) # D
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.4375)) # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.4375)) # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.4375)) # C

# Bar 4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875)) # D
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1875)) # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875)) # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.1875)) # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875)) # D
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.6875)) # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.6875)) # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.6875)) # C

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Dm7: D F A C
# Motif: D -> F -> A -> C (but not all at once)
# First bar: D and A on beat 1, leave C and F hanging
# Second bar: F and C, leave D and A hanging
# Third bar: D and A, leave C and F hanging
# Fourth bar: Finish with F and C

sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.6875), # A
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.4375), # F
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.4375), # C
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.8125, end=2.9375), # D
    pretty_midi.Note(velocity=110, pitch=69, start=2.8125, end=2.9375), # A
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.25), # F
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.25), # C
    pretty_midi.Note(velocity=110, pitch=62, start=4.375, end=4.5), # D
    pretty_midi.Note(velocity=110, pitch=69, start=4.375, end=4.5), # A
    pretty_midi.Note(velocity=110, pitch=65, start=4.625, end=4.75), # F
    pretty_midi.Note(velocity=110, pitch=72, start=4.625, end=4.75), # C
]

sax.notes.extend(sax_notes)

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
