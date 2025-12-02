
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D3
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb3
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # F#3
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # A3
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # B3
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # C#4
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # D4
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # B3
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A3
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F#3
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.625), # Eb3
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D3
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A3 - D7 (A D F# B)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # B3
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # F#4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A3
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # B3
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # F#4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # A3
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # B3
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # A3
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # B3
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A3
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # B3
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # F#4
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif - start it, leave it hanging, come back and finish it
# Motif: D - F# - A - D (half note, quarter note, eighth note, eighth note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=3.0),  # D3 (half note)
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375), # F#3 (eighth)
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75), # A3 (eighth)
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125), # D3 (eighth)
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # D3 (eighth)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    # Hihat on every eighth
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
