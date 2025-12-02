
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
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=45, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0), # A

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.375), # A#
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5), # D

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.875), # D#
    pretty_midi.Note(velocity=80, pitch=56, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=6.0), # G
]

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=59, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25), # B
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # D

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75), # D#
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # F

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25), # A#
]

# Saxophone (Dante): melody that begins with restraint, builds with tension, and resolves
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75), # B
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0), # B
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.125), # A

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25), # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0), # G

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75), # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0), # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5), # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75), # B
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0), # A
]

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Kick on 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 1.5))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.5))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875))

# Add notes to instruments
for note in drum_notes:
    drums.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
