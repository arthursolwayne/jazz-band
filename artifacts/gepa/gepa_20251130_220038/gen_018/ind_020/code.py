
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36   # Kick drum
snare = 38  # Snare drum
hihat = 42  # Hi-hat

# == BAR 1 (0.0 - 1.5s): Little Ray alone ==
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # in seconds

# Drums
drum_notes = [
    (kick, 0.0), (hihat, 0.125), (hihat, 0.25), (hihat, 0.375),
    (snare, 0.5), (hihat, 0.625), (hihat, 0.75), (hihat, 0.875),
    (kick, 1.0), (hihat, 1.125), (hihat, 1.25), (hihat, 1.375),
    (snare, 1.5)
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

# == BAR 2-4 (1.5 - 6.0s): Full quartet ==
# Time starts at 1.5s

# == BASS LINE: Marcus (walking line, chromatic approaches, no repeated notes) ==
bass_notes = [
    (64, 1.5), (63, 1.75), (65, 2.0), (62, 2.25),  # Dm7 chord walk
    (64, 2.5), (63, 2.75), (65, 3.0), (62, 3.25),  # Dm7
    (64, 3.5), (63, 3.75), (65, 4.0), (62, 4.25),  # Dm7
    (64, 4.5), (63, 4.75), (65, 5.0), (62, 5.25)   # Dm7
]

for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# == PIANO: Diane (7th chords, comp on 2 and 4) ==
# Dm7 = D, F, A, C
# Comp on beats 2 and 4 of each bar

piano_notes = [
    # Bar 2: Dm7 on beat 2 (1.75s)
    (62, 1.75), (64, 1.75), (65, 1.75), (67, 1.75),
    # Bar 2: Dm7 on beat 4 (2.25s)
    (62, 2.25), (64, 2.25), (65, 2.25), (67, 2.25),
    # Bar 3: Dm7 on beat 2 (2.75s)
    (62, 2.75), (64, 2.75), (65, 2.75), (67, 2.75),
    # Bar 3: Dm7 on beat 4 (3.25s)
    (62, 3.25), (64, 3.25), (65, 3.25), (67, 3.25),
    # Bar 4: Dm7 on beat 2 (3.75s)
    (62, 3.75), (64, 3.75), (65, 3.75), (67, 3.75),
    # Bar 4: Dm7 on beat 4 (4.25s)
    (62, 4.25), (64, 4.25), (65, 4.25), (67, 4.25)
]

for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.1)
    piano.notes.append(note)

# == DRUMS: Little Ray (fill the bar, kick on 1 and 3, snare on 2 and 4, hihat on every eighth) ==
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    (kick, 1.5), (hihat, 1.625), (hihat, 1.75), (hihat, 1.875),
    (snare, 2.0), (hihat, 2.125), (hihat, 2.25), (hihat, 2.375),
    (kick, 2.5), (hihat, 2.625), (hihat, 2.75), (hihat, 2.875),
    (snare, 3.0)
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    (kick, 3.0), (hihat, 3.125), (hihat, 3.25), (hihat, 3.375),
    (snare, 3.5), (hihat, 3.625), (hihat, 3.75), (hihat, 3.875),
    (kick, 4.0), (hihat, 4.125), (hihat, 4.25), (hihat, 4.375),
    (snare, 4.5)
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    (kick, 4.5), (hihat, 4.625), (hihat, 4.75), (hihat, 4.875),
    (snare, 5.0), (hihat, 5.125), (hihat, 5.25), (hihat, 5.375),
    (kick, 5.5), (hihat, 5.625), (hihat, 5.75), (hihat, 5.875),
    (snare, 6.0)
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

# == SAX: Dante (Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.) ==
# Dm scale: D E F G A Bb C
# Motif: D - E - F - D (1 bar), then repeat with a slight variation

sax_notes = [
    (62, 1.5), (64, 1.75), (64, 2.0), (62, 2.25),  # First iteration
    (62, 2.5), (64, 2.75), (65, 3.0), (62, 3.25),  # Second iteration
    (62, 3.5), (64, 3.75), (64, 4.0), (62, 4.25),  # Third iteration
    (62, 4.5), (64, 4.75), (65, 5.0), (62, 5.25)   # Fourth iteration
]

for pitch, time in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments = [sax, bass, piano, drums]

# Save to a MIDI file
midi.write("dante_intro.mid")
