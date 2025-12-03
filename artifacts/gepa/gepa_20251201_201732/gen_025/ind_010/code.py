
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1: 0.0 - 1.5s
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

# Add drum notes
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (F, Ab, D, C), with chromatic approaches
bass_notes = [
    # Bar 2: 1.5 - 3.0s
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F (1)
    pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.25), # Eb (2)
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625), # D (3)
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # C (4)
    
    # Bar 3: 3.0 - 4.5s
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # F (1)
    pretty_midi.Note(velocity=90, pitch=37, start=3.375, end=3.75), # Eb (2)
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125), # D (3)
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),  # C (4)
    
    # Bar 4: 4.5 - 6.0s
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F (1)
    pretty_midi.Note(velocity=90, pitch=37, start=4.875, end=5.25), # Eb (2)
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625), # D (3)
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),  # C (4)
]

# Add bass notes
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.5 + 0.125), # F (53)
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.5 + 0.125), # Ab (48)
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=1.5 + 0.125), # C (52)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.5 + 0.125), # Eb (50)
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.0 + 0.125), # Bb (51)
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.0 + 0.125), # D (55)
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.0 + 0.125), # F (53)
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.0 + 0.125), # Ab (48)
])

# Bar 4: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.5 + 0.125), # G (55)
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=4.5 + 0.125), # Bb (51)
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.5 + 0.125), # D (58)
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.5 + 0.125), # F (53)
])

# Add piano notes
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F, Ab, Bb, C -> F, Ab, Bb, C (with a slight delay on the last note)

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.625), # F (53)
    pretty_midi.Note(velocity=100, pitch=48, start=1.625, end=1.75), # Ab (48)
    pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=1.875), # Bb (50)
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.0),  # C (52)
    
    # Repeat the motif but leave the last note hanging
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.125), # F (53)
    pretty_midi.Note(velocity=100, pitch=48, start=3.125, end=3.25), # Ab (48)
    pretty_midi.Note(velocity=100, pitch=50, start=3.25, end=3.375), # Bb (50)
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.5),  # C (52)
    
    # Come back and finish the motif
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.625), # F (53)
    pretty_midi.Note(velocity=100, pitch=48, start=4.625, end=4.75), # Ab (48)
    pretty_midi.Note(velocity=100, pitch=50, start=4.75, end=4.875), # Bb (50)
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.0),  # C (52)
]

# Add sax notes
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
