
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(100, 36, time, time + 0.125))  # Kick
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(100, 38, time, time + 0.125))  # Snare
        drum_notes.append(pretty_midi.Note(100, 42, time, time + 0.125))  # Hihat

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = []
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if bar == 2:
            if beat == 0:
                bass_notes.append(pretty_midi.Note(100, 43, time, time + 0.25))  # G2 (Dmaj7 root)
            elif beat == 1:
                bass_notes.append(pretty_midi.Note(100, 42, time, time + 0.25))  # F#2 (chromatic approach)
            elif beat == 2:
                bass_notes.append(pretty_midi.Note(100, 38, time, time + 0.25))  # D2 (Dmaj7 root)
            elif beat == 3:
                bass_notes.append(pretty_midi.Note(100, 40, time, time + 0.25))  # F2 (Dmaj7 3rd)
        elif bar == 3:
            if beat == 0:
                bass_notes.append(pretty_midi.Note(100, 43, time, time + 0.25))  # G2 (Dmaj7 root)
            elif beat == 1:
                bass_notes.append(pretty_midi.Note(100, 42, time, time + 0.25))  # F#2 (chromatic approach)
            elif beat == 2:
                bass_notes.append(pretty_midi.Note(100, 38, time, time + 0.25))  # D2 (Dmaj7 root)
            elif beat == 3:
                bass_notes.append(pretty_midi.Note(100, 40, time, time + 0.25))  # F2 (Dmaj7 3rd)
        elif bar == 4:
            if beat == 0:
                bass_notes.append(pretty_midi.Note(100, 43, time, time + 0.25))  # G2 (Dmaj7 root)
            elif beat == 1:
                bass_notes.append(pretty_midi.Note(100, 42, time, time + 0.25))  # F#2 (chromatic approach)
            elif beat == 2:
                bass_notes.append(pretty_midi.Note(100, 38, time, time + 0.25))  # D2 (Dmaj7 root)
            elif beat == 3:
                bass_notes.append(pretty_midi.Note(100, 40, time, time + 0.25))  # F2 (Dmaj7 3rd)

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = []
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0:
            if bar == 2:
                piano_notes.append(pretty_midi.Note(100, 55, time, time + 0.25))  # D4 (Dmaj7 root)
                piano_notes.append(pretty_midi.Note(100, 62, time, time + 0.25))  # A4 (Dmaj7 5th)
                piano_notes.append(pretty_midi.Note(100, 67, time, time + 0.25))  # D5 (Dmaj7 root octave)
                piano_notes.append(pretty_midi.Note(100, 72, time, time + 0.25))  # F#5 (Dmaj7 3rd)
            elif bar == 3:
                piano_notes.append(pretty_midi.Note(100, 55, time, time + 0.25))  # D4 (D7 root)
                piano_notes.append(pretty_midi.Note(100, 67, time, time + 0.25))  # D5 (D7 root octave)
                piano_notes.append(pretty_midi.Note(100, 72, time, time + 0.25))  # F#5 (D7 3rd)
                piano_notes.append(pretty_midi.Note(100, 76, time, time + 0.25))  # A5 (D7 5th)
            elif bar == 4:
                piano_notes.append(pretty_midi.Note(100, 55, time, time + 0.25))  # D4 (Dmaj7 root)
                piano_notes.append(pretty_midi.Note(100, 62, time, time + 0.25))  # A4 (Dmaj7 5th)
                piano_notes.append(pretty_midi.Note(100, 67, time, time + 0.25))  # D5 (Dmaj7 root octave)
                piano_notes.append(pretty_midi.Note(100, 72, time, time + 0.25))  # F#5 (Dmaj7 3rd)

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
for bar in range(2, 5):
    time = bar * 1.5
    if bar == 2:
        sax_notes.append(pretty_midi.Note(100, 62, time, time + 0.375))  # A4
        sax_notes.append(pretty_midi.Note(100, 67, time + 0.75, time + 1.125))  # D5
        sax_notes.append(pretty_midi.Note(100, 62, time + 1.5, time + 1.875))  # A4
    elif bar == 3:
        sax_notes.append(pretty_midi.Note(100, 67, time, time + 0.375))  # D5
        sax_notes.append(pretty_midi.Note(100, 72, time + 0.75, time + 1.125))  # F#5
        sax_notes.append(pretty_midi.Note(100, 67, time + 1.5, time + 1.875))  # D5
    elif bar == 4:
        sax_notes.append(pretty_midi.Note(100, 62, time, time + 0.375))  # A4
        sax_notes.append(pretty_midi.Note(100, 67, time + 0.75, time + 1.125))  # D5
        sax_notes.append(pretty_midi.Note(100, 72, time + 1.5, time + 1.875))  # F#5

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
