
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line, chromatic approaches, 4 bars = 16 beats
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.75, end=2.0), # F#
    pretty_midi.Note(velocity=100, pitch=46, start=2.0, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.5), # G#
    pretty_midi.Note(velocity=100, pitch=48, start=2.5, end=2.75), # A
    pretty_midi.Note(velocity=100, pitch=49, start=2.75, end=3.0), # A#
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25), # B
    pretty_midi.Note(velocity=100, pitch=51, start=3.25, end=3.5), # C
    pretty_midi.Note(velocity=100, pitch=52, start=3.5, end=3.75), # C#
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.0), # D
    pretty_midi.Note(velocity=100, pitch=54, start=4.0, end=4.25), # D#
    pretty_midi.Note(velocity=100, pitch=55, start=4.25, end=4.5), # E
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.75), # F
    pretty_midi.Note(velocity=100, pitch=57, start=4.75, end=5.0), # F#
    pretty_midi.Note(velocity=100, pitch=58, start=5.0, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.5), # G#
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75), # F7 - F
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75), # F7 - A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75), # F7 - C
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75), # F7 - Bb
    # Bar 3 (2.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75), # F7 - F
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75), # F7 - A
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75), # F7 - C
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75), # F7 - Bb
    # Bar 4 (4.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25), # F7 - F
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25), # F7 - A
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25), # F7 - C
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25), # F7 - Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - Motif that whispers then cries. Start it, leave it hanging, come back and finish.
sax_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=1.625, end=1.75), # E
    # Bar 3 (2.5 - 2.75s)
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75), # C
    # Bar 4 (4.5 - 5.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.75), # E
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0), # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4 (1.5 - 6.0s)
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.875), # Snare on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.375), # Snare on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.875), # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Add hi-hat on every eighth
for i in range(16):
    start = 1.5 + (i * 0.375)
    end = start + 0.1875
    if i % 2 == 0:
        pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
