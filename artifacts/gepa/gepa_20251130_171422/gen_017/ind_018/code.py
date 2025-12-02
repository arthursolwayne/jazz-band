
import pretty_midi

# Create a MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# MIDI note numbers for drums
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Only drums (0.0 - 1.5s)
# Little Ray sets the mood
drum_notes = [
    (KICK, 0.0), (SNARE, 0.5), (HIHAT, 0.0), (HIHAT, 0.25),
    (HIHAT, 0.5), (HIHAT, 0.75), (KICK, 1.0), (SNARE, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.75), (63, 2.0), (60, 2.25),  # Dm7
    (62, 2.5), (64, 2.75), (63, 3.0), (60, 3.25),  # Dm7
    (62, 3.5), (64, 3.75), (63, 4.0), (60, 4.25),  # Dm7
    (62, 4.5), (64, 4.75), (63, 5.0), (60, 5.25)   # Dm7
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Diane, 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D-F-A-C)
    (50, 1.75), (53, 1.75), (57, 1.75), (59, 1.75),
    # Bar 3: Dm7 (same)
    (50, 3.25), (53, 3.25), (57, 3.25), (59, 3.25),
    # Bar 4: Dm7 (same)
    (50, 4.75), (53, 4.75), (57, 4.75), (59, 4.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums in Bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=KICK, start=bar_start, end=bar_start + 0.25)
    kick3 = pretty_midi.Note(velocity=100, pitch=KICK, start=bar_start + 0.75, end=bar_start + 1.0)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_start + 0.5, end=bar_start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_start + 1.25, end=bar_start + 1.5)
    # Hi-hat on every eighth
    for i in range(0, 6):
        hihat = pretty_midi.Note(velocity=100, pitch=HIHAT, start=bar_start + i * 0.25, end=bar_start + i * 0.25 + 0.25)
        drums.notes.append(hihat)
    # Add the kicks and snares
    drums.notes.append(kick1)
    drums.notes.append(kick3)
    drums.notes.append(snare2)
    drums.notes.append(snare4)

# Sax: Dante's melody (start at bar 2)
# Short motif, leave it hanging
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0), (64, 2.25),  # D - F - D - F
    (62, 2.5), (64, 2.75), (62, 3.0), (64, 3.25),  # Repeat the motif
    (62, 3.5), (64, 3.75), (62, 4.0), (64, 4.25),  # Repeat again, leaving it hanging
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
