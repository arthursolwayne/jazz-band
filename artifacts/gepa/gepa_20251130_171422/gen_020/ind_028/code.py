
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Snare on 2 and 4, hihat on every eighth, kick on 3 only for tension
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),     # hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),   # snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: sax starts with a short motif (Fm7 - Bb - Eb - D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=110, pitch=59, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=110, pitch=59, start=3.25, end=3.5),  # C
]

# Bar 2: Marcus plays walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=44, start=3.25, end=3.5),  # C
]

# Bar 2: Diane plays F7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=71, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=95, pitch=71, start=3.25, end=3.5),  # D
]

# Bar 3: sax continues with more tension, lower register
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=48, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=49, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=110, pitch=47, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=45, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=110, pitch=48, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=49, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=47, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=45, start=5.25, end=5.5),  # D
])

# Bar 3: Marcus continues walking bass
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=48, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=44, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.5),  # C
])

# Bar 3: Diane plays F7 on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=95, pitch=71, start=5.25, end=5.5),  # D
])

# Bar 4: sax resolves with a few notes, lingering on D
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=50, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=110, pitch=49, start=5.75, end=6.0),  # F
])

# Bar 4: Marcus plays walking bass
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=48, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=5.75, end=6.0),  # Eb
])

# Bar 4: Diane plays F7 on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=64, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=5.75, end=6.0),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=5.75, end=6.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=71, start=5.75, end=6.0),  # D
])

# Bar 4: Drums continue
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.75),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # snare on 4
])

# Add the notes to the instruments
for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_intro.mid")
