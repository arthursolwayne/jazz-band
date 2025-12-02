
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drum notes: kick=36, snare=38, hihat=42
# Bar divisions: 0.0 - 1.5s (Bar 1), 1.5 - 3.0s (Bar 2), 3.0 - 4.5s (Bar 3), 4.5 - 6.0s (Bar 4)

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Create tension with syncopated hihat, sparse kick and snare
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),    # Kick on 1
    pretty_midi.Note(velocity=85, pitch=38, start=0.75, end=1.125),   # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),      # Hihat on every 8th
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full ensemble enters (1.5 - 3.0s)
# Sax plays a motive that lingers — Dm7, Bb, C, Ab (Dm7 -> Bbmaj7 -> Cm7 -> Ab7)

# Saxophone motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),    # D (Dm7)
    pretty_midi.Note(velocity=100, pitch=57, start=1.75, end=2.0),    # Bb (Bbmaj7)
    pretty_midi.Note(velocity=100, pitch=60, start=2.125, end=2.375), # C (Cm7)
    pretty_midi.Note(velocity=100, pitch=55, start=2.5, end=2.75),    # Ab (Ab7)
]

for note in sax_notes:
    sax.notes.append(note)

# Marcus: Walking bass line in Dm, chromatic approach to D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),    # C
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),    # C#
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),    # D
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),    # C
    pretty_midi.Note(velocity=80, pitch=47, start=2.5, end=2.75),    # B
    pretty_midi.Note(velocity=80, pitch=48, start=2.75, end=3.0),    # C
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Comping with 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),    # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),    # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),    # A
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),    # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),    # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),    # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),    # A
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),    # C
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Continue the ensemble, add tension and space
# Sax plays a variation on the motive, more space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),    # D (Dm7)
    pretty_midi.Note(velocity=100, pitch=57, start=3.25, end=3.5),    # Bb (Bbmaj7)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),    # C (Cm7)
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),   # Ab (Ab7)
]

for note in sax_notes:
    sax.notes.append(note)

# Marcus: Chromatic walking line, continues
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),    # D
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5),    # C
    pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.75),    # B
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.0),    # C
    pretty_midi.Note(velocity=80, pitch=49, start=4.0, end=4.25),    # C#
    pretty_midi.Note(velocity=80, pitch=50, start=4.25, end=4.5),    # D
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Comping again, but on different chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),    # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),    # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),    # A
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),    # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),    # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),    # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),    # A
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),    # C
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Resolution, with space and a lingering note
# Sax ends on the Ab, unresolved but haunting
# Drums continue with rhythmic energy

# Saxophone ending note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=5.0),    # Ab (Ab7)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Energy continues, no resolution
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),    # Kick on 1
    pretty_midi.Note(velocity=85, pitch=38, start=5.0, end=5.375),    # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=6.0),      # Hihat on every 8th
    pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
