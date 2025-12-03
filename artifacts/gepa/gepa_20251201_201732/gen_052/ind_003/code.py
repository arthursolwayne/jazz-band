
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=76, start=1.875, end=2.25),  # C3
    pretty_midi.Note(velocity=80, pitch=75, start=2.25, end=2.625),  # Bb3
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),  # F2
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=80, pitch=80, start=3.375, end=3.75),  # F3
    pretty_midi.Note(velocity=80, pitch=79, start=3.75, end=4.125),  # Eb3
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.5),  # C3
    pretty_midi.Note(velocity=80, pitch=80, start=4.5, end=4.875),  # F3
    pretty_midi.Note(velocity=80, pitch=84, start=4.875, end=5.25),  # A3
    pretty_midi.Note(velocity=80, pitch=83, start=5.25, end=5.625),  # G3
    pretty_midi.Note(velocity=80, pitch=80, start=5.625, end=6.0),  # F3
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: open voicings, resolve on the last beat of each bar
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=80, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),
    # Bar 4 (continued): resolve to Fmaj7 again
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=80, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),
    # Resolve to Fmaj7 at the end
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=80, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: short motif, start, leave it hanging, return and finish
# F7 (F, A, C, Eb) in 8th notes with a half note on the last beat
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=73, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=6.0),     # F (sustained)
]
for note in sax_notes:
    sax.notes.append(note)

# Add the final drum fill
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
