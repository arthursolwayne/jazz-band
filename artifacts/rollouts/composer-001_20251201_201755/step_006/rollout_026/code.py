
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),   # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # F2 (fifth of D2)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),   # G2
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),  # A2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125),  # B2
    pretty_midi.Note(velocity=90, pitch=44, start=4.125, end=4.5),   # D3 (fifth of G2)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875),   # D3
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.25),  # E3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625),  # F#3
    pretty_midi.Note(velocity=90, pitch=49, start=5.625, end=6.0),   # A3 (fifth of D3)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # A (MIDI 76)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.25),  # C (MIDI 79)
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=2.25),  # E (MIDI 82)
]

# Bar 3: Dm7 (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # D (MIDI 67)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75),  # A (MIDI 76)
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.75),  # C (MIDI 79)
])

# Bar 4: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.25),  # G (MIDI 74)
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=5.25),  # B (MIDI 78)
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=5.25),  # D (MIDI 79)
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=5.25),  # F (MIDI 82)
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (71), A (76), D (70), F (71)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # F (return)
    pretty_midi.Note(velocity=110, pitch=76, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=110, pitch=70, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
