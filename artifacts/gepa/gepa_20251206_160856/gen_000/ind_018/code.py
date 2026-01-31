
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # F2 (chromatic approach)
    
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # F2
    
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # F2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C5
]

# Bar 3: G7 (G-B-D-F)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4
]

# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # Bb4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - A4 - D5 (suspension on the last note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0),  # D5
]

# Repeat the motif, but with a slight variation
sax_notes += [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.5),  # D5
]

# Repeat again, with a slight rest before the final note
sax_notes += [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0),  # D5
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = []

# Bar 2
for i in range(4):
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i*0.375, end=1.5 + i*0.375 + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5 + i*0.375 + 0.375, end=1.5 + i*0.375 + 0.375 + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5 + i*0.375, end=1.5 + i*0.375 + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5 + i*0.375 + 0.375, end=1.5 + i*0.375 + 0.375 + 0.375))

# Bar 3
for i in range(4):
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0 + i*0.375, end=3.0 + i*0.375 + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.0 + i*0.375 + 0.375, end=3.0 + i*0.375 + 0.375 + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0 + i*0.375, end=3.0 + i*0.375 + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0 + i*0.375 + 0.375, end=3.0 + i*0.375 + 0.375 + 0.375))

# Bar 4
for i in range(4):
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5 + i*0.375, end=4.5 + i*0.375 + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5 + i*0.375 + 0.375, end=4.5 + i*0.375 + 0.375 + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5 + i*0.375, end=4.5 + i*0.375 + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5 + i*0.375 + 0.375, end=4.5 + i*0.375 + 0.375 + 0.375))

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
