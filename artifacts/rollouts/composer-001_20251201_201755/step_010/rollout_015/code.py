
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),    # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full band enters
# Bass line: Marcus on D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D2 (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane, open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # B4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # D4
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25), # F4
    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # C4
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625), # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # Bb4 (resolve from B4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),   # A4 (start of motif)
    pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=2.0),   # C5 (next note)
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),   # A4 (return)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # G4 (finish motif)
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # D4 (resolve)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: continue in bars 2-4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.5),    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.375, end=2.75), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.375, end=2.75), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=3.125), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.75, end=3.0),   # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
