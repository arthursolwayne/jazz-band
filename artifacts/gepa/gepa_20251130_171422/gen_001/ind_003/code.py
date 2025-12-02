
import pretty_midi
from pretty_midi import Note, Instrument

# Create a Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Create instruments
bass_instrument = Instrument(program=33, is_drum=False, name='Bass')
piano_instrument = Instrument(program=0, is_drum=False, name='Piano')
drums_instrument = Instrument(program=0, is_drum=True, name='Drums')
sax_instrument = Instrument(program=64, is_drum=False, name='Saxophone')

# Add instruments to the PrettyMIDI object
pm.instruments = [bass_instrument, piano_instrument, drums_instrument, sax_instrument]

# Time per bar: 1.5 seconds (160 BPM, 4/4)
bar_length = 1.5
note_duration = 0.375  # 1/4 note

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    Note(36, 0.0, note_duration),  # Kick on 1
    Note(38, 0.375, note_duration),  # Snare on 2
    Note(42, 0.0, note_duration / 2),  # Hihat on 1 &
    Note(42, 0.375, note_duration / 2),  # Hihat on 2 &
    Note(36, 0.75, note_duration),  # Kick on 3
    Note(38, 1.125, note_duration),  # Snare on 4
    Note(42, 0.75, note_duration / 2),  # Hihat on 3 &
    Note(42, 1.125, note_duration / 2),  # Hihat on 4 &
]
for note in drum_notes:
    drums_instrument.notes.append(note)

# Bar 2: Bass enters
# Walking bass line, chromatic approaches
bass_notes = [
    Note(45, 1.5, note_duration),  # F
    Note(47, 1.875, note_duration),  # G#
    Note(46, 2.25, note_duration),  # G
    Note(44, 2.625, note_duration),  # E
]
for note in bass_notes:
    bass_instrument.notes.append(note)

# Bar 2: Piano enters
# 7th chords, comp on 2 and 4
piano_notes = [
    Note(71, 1.875, note_duration / 2),  # F7: F, A, C, E
    Note(73, 1.875, note_duration / 2),
    Note(72, 1.875, note_duration / 2),
    Note(69, 1.875, note_duration / 2),
    Note(71, 2.625, note_duration / 2),
    Note(73, 2.625, note_duration / 2),
    Note(72, 2.625, note_duration / 2),
    Note(69, 2.625, note_duration / 2),
]
for note in piano_notes:
    piano_instrument.notes.append(note)

# Bar 2: Sax enters with motif
# Motif: F - Bb - Eb - rest
sax_notes = [
    Note(69, 1.5, note_duration / 2),  # F
    Note(64, 1.875, note_duration / 2),  # Bb
    Note(60, 2.25, note_duration / 2),  # Eb
]
for note in sax_notes:
    sax_instrument.notes.append(note)

# Bar 3: Continue bass
bass_notes = [
    Note(47, 2.625, note_duration),  # G#
    Note(49, 2.999, note_duration),  # A#
    Note(48, 3.375, note_duration),  # A
    Note(46, 3.75, note_duration),  # G
]
for note in bass_notes:
    bass_instrument.notes.append(note)

# Bar 3: Continue piano
piano_notes = [
    Note(71, 3.375, note_duration / 2),
    Note(73, 3.375, note_duration / 2),
    Note(72, 3.375, note_duration / 2),
    Note(69, 3.375, note_duration / 2),
    Note(71, 4.125, note_duration / 2),
    Note(73, 4.125, note_duration / 2),
    Note(72, 4.125, note_duration / 2),
    Note(69, 4.125, note_duration / 2),
]
for note in piano_notes:
    piano_instrument.notes.append(note)

# Bar 3: Continue drums
drum_notes = [
    Note(36, 3.0, note_duration),  # Kick on 1
    Note(38, 3.375, note_duration),  # Snare on 2
    Note(42, 3.0, note_duration / 2),  # Hihat on 1 &
    Note(42, 3.375, note_duration / 2),  # Hihat on 2 &
    Note(36, 3.75, note_duration),  # Kick on 3
    Note(38, 4.125, note_duration),  # Snare on 4
    Note(42, 3.75, note_duration / 2),  # Hihat on 3 &
    Note(42, 4.125, note_duration / 2),  # Hihat on 4 &
]
for note in drum_notes:
    drums_instrument.notes.append(note)

# Bar 3: Continue sax
# Motif continuation: F - Bb - Eb - rest, then F again
sax_notes = [
    Note(69, 3.75, note_duration),  # F
]
for note in sax_notes:
    sax_instrument.notes.append(note)

# Bar 4: Continue bass
bass_notes = [
    Note(49, 4.125, note_duration),  # A#
    Note(51, 4.5, note_duration),  # B
    Note(50, 4.875, note_duration),  # Bb
    Note(48, 5.25, note_duration),  # A
]
for note in bass_notes:
    bass_instrument.notes.append(note)

# Bar 4: Continue piano
piano_notes = [
    Note(71, 4.875, note_duration / 2),
    Note(73, 4.875, note_duration / 2),
    Note(72, 4.875, note_duration / 2),
    Note(69, 4.875, note_duration / 2),
    Note(71, 5.625, note_duration / 2),
    Note(73, 5.625, note_duration / 2),
    Note(72, 5.625, note_duration / 2),
    Note(69, 5.625, note_duration / 2),
]
for note in piano_notes:
    piano_instrument.notes.append(note)

# Bar 4: Continue drums
drum_notes = [
    Note(36, 4.5, note_duration),  # Kick on 1
    Note(38, 4.875, note_duration),  # Snare on 2
    Note(42, 4.5, note_duration / 2),  # Hihat on 1 &
    Note(42, 4.875, note_duration / 2),  # Hihat on 2 &
    Note(36, 5.25, note_duration),  # Kick on 3
    Note(38, 5.625, note_duration),  # Snare on 4
    Note(42, 5.25, note_duration / 2),  # Hihat on 3 &
    Note(42, 5.625, note_duration / 2),  # Hihat on 4 &
]
for note in drum_notes:
    drums_instrument.notes.append(note)

# Bar 4: Sax finishes the motif
sax_notes = [
    Note(69, 5.25, note_duration / 2),  # F
    Note(64, 5.625, note_duration / 2),  # Bb
]
for note in sax_notes:
    sax_instrument.notes.append(note)

# Write the MIDI file
pm.write("dante_intro.mid")
